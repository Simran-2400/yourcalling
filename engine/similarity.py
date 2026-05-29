# YourCalling — Similarity Engine
# Pure tag-based cross-media matching. No external APIs.
# Variable naming: S prefix (inputs), V prefix (computed values)

from data.catalog import CATALOG


def V_compute_jaccard(S_tags_a: list, S_tags_b: list) -> float:
    """Jaccard similarity between two tag lists."""
    V_set_a = set(S_tags_a)
    V_set_b = set(S_tags_b)
    V_intersection = V_set_a & V_set_b
    V_union = V_set_a | V_set_b
    if not V_union:
        return 0.0
    return len(V_intersection) / len(V_union)


def V_compute_weighted_score(S_item_a: dict, S_item_b: dict) -> float:
    """
    Weighted similarity scoring:
    - Jaccard tag overlap (core)
    - Bonus for mood/emotion alignment (top 5 emotional tags)
    - Cross-media bonus (rewards diversity in recommendations)
    """
    V_jaccard = V_compute_jaccard(S_item_a["tags"], S_item_b["tags"])

    # Emotional anchor tags (highest signal for cross-media feel matching)
    V_emotional_anchors = {
        "melancholic", "dark", "hopeful", "romantic", "bittersweet",
        "longing", "grief", "joyful", "peaceful", "intense", "haunting",
        "whimsical", "nostalgia", "serene", "tragic", "beautiful", "dark",
        "triumphant", "philosophical", "introspective", "surreal"
    }
    V_mood_a = set(S_item_a["tags"]) & V_emotional_anchors
    V_mood_b = set(S_item_b["tags"]) & V_emotional_anchors
    V_mood_union = V_mood_a | V_mood_b
    V_mood_score = (
        len(V_mood_a & V_mood_b) / len(V_mood_union)
        if V_mood_union else 0.0
    )

    # Cross-media bonus: slightly reward if media type differs
    V_cross_bonus = 0.05 if S_item_a["media"] != S_item_b["media"] else 0.0

    V_final_score = (0.60 * V_jaccard) + (0.35 * V_mood_score) + V_cross_bonus
    return round(V_final_score, 4)


def V_get_recommendations(
    S_input_title: str,
    S_n_results: int = 4,
    S_lang_filter: list = None,
    S_media_filter: list = None,
    S_ensure_cross_media: bool = True,
) -> dict:
    """
    Main recommendation function.

    Parameters
    ----------
    S_input_title      : str   — exact or partial title to search
    S_n_results        : int   — number of recommendations to return
    S_lang_filter      : list  — filter by languages e.g. ["en", "it"]
    S_media_filter     : list  — filter by media type e.g. ["book", "song"]
    S_ensure_cross_media: bool — ensure at least one result per media category

    Returns
    -------
    dict with keys: input_item, recommendations, not_found (bool)
    """

    # ── 1. Find input item in catalog ────────────────────────────────────────
    S_query = S_input_title.strip().lower()
    V_matched_item = None
    for V_item in CATALOG:
        if S_query in V_item["title"].lower():
            V_matched_item = V_item
            break

    if V_matched_item is None:
        return {"input_item": None, "recommendations": [], "not_found": True}

    # ── 2. Build candidate pool (exclude input item itself) ──────────────────
    V_candidates = [
        V_item for V_item in CATALOG
        if V_item["id"] != V_matched_item["id"]
    ]

    # Apply language filter if specified
    if S_lang_filter:
        V_candidates = [
            V_c for V_c in V_candidates if V_c["lang"] in S_lang_filter
        ]

    # Apply media filter if specified
    if S_media_filter:
        V_candidates = [
            V_c for V_c in V_candidates if V_c["media"] in S_media_filter
        ]

    # ── 3. Score all candidates ───────────────────────────────────────────────
    V_scored = []
    for V_candidate in V_candidates:
        V_score = V_compute_weighted_score(V_matched_item, V_candidate)
        V_shared_tags = sorted(
            set(V_matched_item["tags"]) & set(V_candidate["tags"])
        )
        V_scored.append({
            "item": V_candidate,
            "score": V_score,
            "shared_tags": V_shared_tags,
            "shared_count": len(V_shared_tags),
        })

    V_scored.sort(key=lambda V_x: V_x["score"], reverse=True)

    # ── 4. Cross-media diversity enforcement ─────────────────────────────────
    # Enforce diversity when: no filter, OR multiple media types selected
    V_do_diversity = S_ensure_cross_media and (
        not S_media_filter or len(S_media_filter) > 1
    )
    if V_do_diversity:
        V_media_types = ["book", "movie", "song"]
        V_results = []
        V_seen_media = set()

        # First pass: grab best from each media type
        for V_media in V_media_types:
            for V_entry in V_scored:
                if (
                    V_entry["item"]["media"] == V_media
                    and V_entry["item"]["id"] not in {V_r["item"]["id"] for V_r in V_results}
                ):
                    V_results.append(V_entry)
                    V_seen_media.add(V_media)
                    break

        # Fill remaining slots with highest-scoring remaining candidates
        V_remaining_needed = S_n_results - len(V_results)
        V_existing_ids = {V_r["item"]["id"] for V_r in V_results}
        for V_entry in V_scored:
            if V_remaining_needed <= 0:
                break
            if V_entry["item"]["id"] not in V_existing_ids:
                V_results.append(V_entry)
                V_remaining_needed -= 1

        # Sort final results by score descending
        V_results.sort(key=lambda V_x: V_x["score"], reverse=True)
        V_final = V_results[:S_n_results]
    else:
        V_final = V_scored[:S_n_results]

    return {
        "input_item": V_matched_item,
        "recommendations": V_final,
        "not_found": False,
    }


def V_search_catalog(S_query: str) -> list:
    """Fuzzy search catalog titles for autocomplete / dropdown."""
    S_q = S_query.strip().lower()
    if not S_q:
        return []
    V_matches = [
        V_item for V_item in CATALOG
        if S_q in V_item["title"].lower()
    ]
    return V_matches[:20]


def V_get_all_titles() -> list:
    """Return all catalog titles for dropdown population."""
    return sorted([V_item["title"] for V_item in CATALOG])


def V_get_catalog_stats() -> dict:
    """Return catalog breakdown statistics."""
    V_stats = {
        "total": len(CATALOG),
        "by_media": {},
        "by_lang": {},
        "by_media_lang": {},
    }
    for V_item in CATALOG:
        V_media = V_item["media"]
        V_lang = V_item["lang"]
        V_key = f"{V_media}_{V_lang}"
        V_stats["by_media"][V_media] = V_stats["by_media"].get(V_media, 0) + 1
        V_stats["by_lang"][V_lang] = V_stats["by_lang"].get(V_lang, 0) + 1
        V_stats["by_media_lang"][V_key] = V_stats["by_media_lang"].get(V_key, 0) + 1
    return V_stats
