# YourCalling — Similarity Engine
# Pure tag-based cross-media matching. No external APIs.

from data.catalog import CATALOG


def compute_jaccard(tags_a: list, tags_b: list) -> float:
    """Jaccard similarity between two tag lists."""
    set_a = set(tags_a)
    set_b = set(tags_b)
    intersection = set_a & set_b
    union = set_a | set_b
    if not union:
        return 0.0
    return len(intersection) / len(union)


def compute_weighted_score(item_a: dict, item_b: dict) -> float:
    """
    Weighted similarity scoring:
    - Jaccard tag overlap (core)
    - Bonus for mood/emotion alignment (top 5 emotional tags)
    - Cross-media bonus (rewards diversity in recommendations)
    """
    jaccard = compute_jaccard(item_a["tags"], item_b["tags"])

    # Emotional anchor tags (highest signal for cross-media feel matching)
    emotional_anchors = {
        "melancholic", "dark", "hopeful", "romantic", "bittersweet",
        "longing", "grief", "joyful", "peaceful", "intense", "haunting",
        "whimsical", "nostalgia", "serene", "tragic", "beautiful", "dark",
        "triumphant", "philosophical", "introspective", "surreal"
    }
    mood_a = set(item_a["tags"]) & emotional_anchors
    mood_b = set(item_b["tags"]) & emotional_anchors
    mood_union = mood_a | mood_b
    mood_score = (
        len(mood_a & mood_b) / len(mood_union)
        if mood_union else 0.0
    )

    # Cross-media bonus: slightly reward if media type differs
    cross_bonus = 0.05 if item_a["media"] != item_b["media"] else 0.0

    final_score = (0.60 * jaccard) + (0.35 * mood_score) + cross_bonus
    return round(final_score, 4)


def get_recommendations(
    input_title: str,
    n_results: int = 4,
    lang_filter: list = None,
    media_filter: list = None,
    ensure_cross_media: bool = True,
) -> dict:
    """
    Main recommendation function.

    Parameters
    ----------
    input_title      : str   — exact or partial title to search
    n_results        : int   — number of recommendations to return
    lang_filter      : list  — filter by languages e.g. ["en", "it"]
    media_filter     : list  — filter by media type e.g. ["book", "song"]
    ensure_cross_media: bool — ensure at least one result per media category

    Returns
    -------
    dict with keys: input_item, recommendations, not_found (bool)
    """

    # 1. Find input item in catalog
    query = input_title.strip().lower()
    matched_item = None
    for item in CATALOG:
        if query in item["title"].lower():
            matched_item = item
            break

    if matched_item is None:
        return {"input_item": None, "recommendations": [], "not_found": True}

    # 2. Build candidate pool (exclude input item itself)
    candidates = [
        item for item in CATALOG
        if item["id"] != matched_item["id"]
    ]

    # Apply language filter if specified
    if lang_filter:
        candidates = [
            c for c in candidates if c["lang"] in lang_filter
        ]

    # Apply media filter if specified
    if media_filter:
        candidates = [
            c for c in candidates if c["media"] in media_filter
        ]

    # 3. Score all candidates
    scored = []
    for candidate in candidates:
        score = compute_weighted_score(matched_item, candidate)
        shared_tags = sorted(
            set(matched_item["tags"]) & set(candidate["tags"])
        )
        scored.append({
            "item": candidate,
            "score": score,
            "shared_tags": shared_tags,
            "shared_count": len(shared_tags),
        })

    scored.sort(key=lambda x: x["score"], reverse=True)

    # 4. Cross-media diversity enforcement
    # Enforce diversity when: no filter, OR multiple media types selected
    do_diversity = ensure_cross_media and (
        not media_filter or len(media_filter) > 1
    )
    if do_diversity:
        media_types = ["book", "movie", "song"]
        results = []
        seen_media = set()

        # First pass: grab best from each media type
        for media in media_types:
            for entry in scored:
                if (
                    entry["item"]["media"] == media
                    and entry["item"]["id"] not in {r["item"]["id"] for r in results}
                ):
                    results.append(entry)
                    seen_media.add(media)
                    break

        # Fill remaining slots with highest-scoring remaining candidates
        remaining_needed = n_results - len(results)
        existing_ids = {r["item"]["id"] for r in results}
        for entry in scored:
            if remaining_needed <= 0:
                break
            if entry["item"]["id"] not in existing_ids:
                results.append(entry)
                remaining_needed -= 1

        # Sort final results by score descending
        results.sort(key=lambda x: x["score"], reverse=True)
        final = results[:n_results]
    else:
        final = scored[:n_results]

    return {
        "input_item": matched_item,
        "recommendations": final,
        "not_found": False,
    }


def search_catalog(query: str) -> list:
    """Fuzzy search catalog titles for autocomplete / dropdown."""
    q = query.strip().lower()
    if not q:
        return []
    matches = [
        item for item in CATALOG
        if q in item["title"].lower()
    ]
    return matches[:20]


def get_all_titles() -> list:
    """Return all catalog titles for dropdown population."""
    return sorted([item["title"] for item in CATALOG])


def get_catalog_stats() -> dict:
    """Return catalog breakdown statistics."""
    stats = {
        "total": len(CATALOG),
        "by_media": {},
        "by_lang": {},
        "by_media_lang": {},
    }
    for item in CATALOG:
        media = item["media"]
        lang = item["lang"]
        key = f"{media}_{lang}"
        stats["by_media"][media] = stats["by_media"].get(media, 0) + 1
        stats["by_lang"][lang] = stats["by_lang"].get(lang, 0) + 1
        stats["by_media_lang"][key] = stats["by_media_lang"].get(key, 0) + 1
    return stats
