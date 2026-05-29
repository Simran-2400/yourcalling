"""
YourCalling — Cross-Media Recommendation Engine
Author : Simran Vishnoi | University of Parma
Course : Data Science for Management
Engine : Pure tag-based Jaccard similarity (no APIs)
UI     : Dark glassmorphism Streamlit
"""

import streamlit as st
from engine.similarity import (
    V_get_recommendations,
    V_get_all_titles,
    V_get_catalog_stats,
)
from data.catalog import CATALOG

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="YourCalling",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Dark Glassmorphism CSS ────────────────────────────────────────────────────
st.markdown("""
<style>
  /* ── Google Fonts ── */
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,600;1,400&display=swap');

  /* ── Root variables ── */
  :root {
    --bg-deep:     #050508;
    --bg-dark:     #0a0a12;
    --glass-bg:    rgba(255,255,255,0.04);
    --glass-bdr:   rgba(255,255,255,0.10);
    --glass-hover: rgba(255,255,255,0.07);
    --accent:      #a78bfa;
    --accent2:     #818cf8;
    --accent3:     #f472b6;
    --text-primary:   #f1f0fb;
    --text-secondary: #a09db8;
    --text-muted:     #5c5870;
    --book-color:  #f472b6;
    --movie-color: #60a5fa;
    --song-color:  #34d399;
    --tag-bg:      rgba(167,139,250,0.12);
    --tag-border:  rgba(167,139,250,0.30);
  }

  /* ── Global reset ── */
  html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: var(--bg-deep) !important;
    color: var(--text-primary) !important;
  }

  .main .block-container {
    padding: 0 2rem 4rem 2rem;
    max-width: 1200px;
    margin: 0 auto;
    background: transparent !important;
  }

  /* Hide Streamlit chrome */
  #MainMenu, header, footer { visibility: hidden; }
  .stDeployButton { display: none; }

  /* ── Hero header ── */
  .yc-hero {
    text-align: center;
    padding: 3.5rem 1rem 2rem 1rem;
    position: relative;
  }
  .yc-hero::before {
    content: '';
    position: absolute;
    top: 0; left: 50%;
    transform: translateX(-50%);
    width: 600px; height: 300px;
    background: radial-gradient(ellipse at 50% 0%, rgba(167,139,250,0.18) 0%, transparent 70%);
    pointer-events: none;
  }
  .yc-logo {
    font-family: 'Playfair Display', serif;
    font-size: 3.8rem;
    font-weight: 600;
    letter-spacing: -0.02em;
    background: linear-gradient(135deg, #e0d7ff 0%, #a78bfa 40%, #818cf8 70%, #f472b6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0;
    line-height: 1.1;
  }
  .yc-tagline {
    font-size: 1.0rem;
    color: var(--text-secondary);
    margin-top: 0.5rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    font-weight: 400;
  }

  /* ── Divider ── */
  .yc-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--glass-bdr), transparent);
    margin: 1.5rem 0;
  }

  /* ── Glass card ── */
  .glass-card {
    background: var(--glass-bg);
    border: 1px solid var(--glass-bdr);
    border-radius: 16px;
    padding: 1.6rem;
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    transition: border-color 0.3s ease, background 0.3s ease;
    margin-bottom: 1rem;
  }
  .glass-card:hover {
    background: var(--glass-hover);
    border-color: rgba(167,139,250,0.30);
  }

  /* ── Section labels ── */
  .yc-section-label {
    font-size: 0.72rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--text-muted);
    font-weight: 600;
    margin-bottom: 0.8rem;
  }

  /* ── Input query display ── */
  .yc-query-card {
    background: linear-gradient(135deg, rgba(167,139,250,0.12), rgba(129,140,248,0.06));
    border: 1px solid rgba(167,139,250,0.30);
    border-radius: 16px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 1rem;
  }
  .yc-query-icon {
    font-size: 2.2rem;
    line-height: 1;
  }
  .yc-query-meta {
    flex: 1;
  }
  .yc-query-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: var(--text-primary);
    margin: 0 0 0.2rem 0;
  }
  .yc-query-sub {
    font-size: 0.82rem;
    color: var(--text-secondary);
  }

  /* ── Recommendation card ── */
  .rec-card {
    background: var(--glass-bg);
    border: 1px solid var(--glass-bdr);
    border-radius: 14px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 0.75rem;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
  }
  .rec-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 3px; height: 100%;
    border-radius: 14px 0 0 14px;
  }
  .rec-card.type-book::before  { background: var(--book-color); }
  .rec-card.type-movie::before { background: var(--movie-color); }
  .rec-card.type-song::before  { background: var(--song-color); }
  .rec-card:hover {
    background: var(--glass-hover);
    border-color: rgba(255,255,255,0.18);
    transform: translateY(-2px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
  }

  .rec-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 0.8rem;
    margin-bottom: 0.5rem;
  }
  .rec-media-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 0.2rem 0.6rem;
    border-radius: 20px;
    white-space: nowrap;
  }
  .badge-book  { background: rgba(244,114,182,0.15); color: var(--book-color);  border: 1px solid rgba(244,114,182,0.30); }
  .badge-movie { background: rgba(96,165,250,0.15);  color: var(--movie-color); border: 1px solid rgba(96,165,250,0.30); }
  .badge-song  { background: rgba(52,211,153,0.15);  color: var(--song-color);  border: 1px solid rgba(52,211,153,0.30); }

  .rec-lang-badge {
    font-size: 0.65rem;
    padding: 0.15rem 0.45rem;
    border-radius: 20px;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.10);
    color: var(--text-muted);
  }

  .rec-title {
    font-size: 1.05rem;
    font-weight: 600;
    color: var(--text-primary);
    margin: 0.1rem 0 0.15rem 0;
  }
  .rec-creator {
    font-size: 0.82rem;
    color: var(--text-secondary);
    margin: 0;
  }

  /* ── Score bar ── */
  .score-container {
    margin: 0.6rem 0 0.5rem 0;
  }
  .score-label {
    display: flex;
    justify-content: space-between;
    font-size: 0.72rem;
    color: var(--text-muted);
    margin-bottom: 0.25rem;
  }
  .score-bar-track {
    height: 4px;
    background: rgba(255,255,255,0.07);
    border-radius: 2px;
    overflow: hidden;
  }
  .score-bar-fill {
    height: 100%;
    border-radius: 2px;
    transition: width 0.6s ease;
  }

  /* ── Tags ── */
  .tags-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.3rem;
    margin-top: 0.5rem;
  }
  .tag-pill {
    font-size: 0.68rem;
    padding: 0.18rem 0.5rem;
    background: var(--tag-bg);
    border: 1px solid var(--tag-border);
    border-radius: 20px;
    color: var(--accent);
    font-weight: 500;
    letter-spacing: 0.03em;
  }
  .tag-pill.shared {
    background: rgba(167,139,250,0.20);
    border-color: rgba(167,139,250,0.50);
    color: #c4b5fd;
  }

  /* ── Stats bar ── */
  .stats-row {
    display: flex;
    gap: 0.8rem;
    flex-wrap: wrap;
    margin: 1.2rem 0;
    justify-content: center;
  }
  .stat-chip {
    background: var(--glass-bg);
    border: 1px solid var(--glass-bdr);
    border-radius: 10px;
    padding: 0.6rem 1rem;
    text-align: center;
    min-width: 90px;
  }
  .stat-num {
    font-size: 1.4rem;
    font-weight: 700;
    background: linear-gradient(135deg, #a78bfa, #818cf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    display: block;
  }
  .stat-label {
    font-size: 0.65rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }

  /* ── Streamlit select + input overrides ── */
  .stSelectbox > div > div,
  .stTextInput > div > div > input {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.10) !important;
    border-radius: 12px !important;
    color: var(--text-primary) !important;
    font-family: 'Inter', sans-serif !important;
  }
  .stSelectbox > div > div:focus-within,
  .stTextInput > div > div > input:focus {
    border-color: rgba(167,139,250,0.50) !important;
    box-shadow: 0 0 0 2px rgba(167,139,250,0.15) !important;
  }

  /* ── Button ── */
  .stButton > button {
    background: linear-gradient(135deg, #7c3aed, #4f46e5) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    letter-spacing: 0.02em !important;
    padding: 0.6rem 2rem !important;
    width: 100% !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 20px rgba(124,58,237,0.35) !important;
  }
  .stButton > button:hover {
    background: linear-gradient(135deg, #8b5cf6, #6366f1) !important;
    box-shadow: 0 6px 28px rgba(124,58,237,0.50) !important;
    transform: translateY(-1px) !important;
  }

  /* ── Expander ── */
  .streamlit-expanderHeader {
    background: transparent !important;
    border: 1px solid var(--glass-bdr) !important;
    border-radius: 10px !important;
    color: var(--text-secondary) !important;
    font-size: 0.82rem !important;
  }
  .streamlit-expanderContent {
    background: var(--glass-bg) !important;
    border: 1px solid var(--glass-bdr) !important;
    border-top: none !important;
    border-radius: 0 0 10px 10px !important;
  }

  /* ── Selectbox label ── */
  .stSelectbox label, .stTextInput label, .stRadio label,
  .stCheckbox label, .stMultiSelect label {
    color: var(--text-secondary) !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.03em !important;
  }

  /* ── No result ── */
  .not-found {
    text-align: center;
    padding: 2.5rem;
    color: var(--text-secondary);
    font-size: 0.95rem;
  }
  .not-found span { font-size: 2.5rem; display: block; margin-bottom: 0.5rem; }

  /* ── Footer ── */
  .yc-footer {
    text-align: center;
    padding: 2rem 0 1rem 0;
    color: var(--text-muted);
    font-size: 0.72rem;
    letter-spacing: 0.06em;
    border-top: 1px solid var(--glass-bdr);
    margin-top: 2rem;
  }

  /* ── Scrollbar ── */
  ::-webkit-scrollbar { width: 6px; }
  ::-webkit-scrollbar-track { background: var(--bg-deep); }
  ::-webkit-scrollbar-thumb { background: rgba(167,139,250,0.30); border-radius: 3px; }
  ::-webkit-scrollbar-thumb:hover { background: rgba(167,139,250,0.50); }
</style>
""", unsafe_allow_html=True)


# ── Helper: media icon + color ────────────────────────────────────────────────
def V_media_icon(S_media: str) -> str:
    return {"book": "📖", "movie": "🎬", "song": "🎵"}.get(S_media, "✦")

def V_media_label(S_media: str) -> str:
    return {"book": "Book", "movie": "Movie", "song": "Song"}.get(S_media, S_media)

def V_lang_label(S_lang: str) -> str:
    return {"en": "EN", "it": "IT", "hi": "HI"}.get(S_lang, S_lang.upper())

def V_score_color(S_score: float) -> str:
    if S_score >= 0.55:
        return "linear-gradient(90deg, #a78bfa, #818cf8)"
    elif S_score >= 0.35:
        return "linear-gradient(90deg, #60a5fa, #818cf8)"
    else:
        return "linear-gradient(90deg, #34d399, #60a5fa)"

def V_score_pct(S_score: float) -> int:
    return min(int(S_score * 200), 100)  # scale 0–0.5 → 0–100%


# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="yc-hero">
  <h1 class="yc-logo">YourCalling</h1>
  <p class="yc-tagline">Cross-Media Recommendation Engine · Books · Movies · Songs</p>
</div>
<div class="yc-divider"></div>
""", unsafe_allow_html=True)

# ── Catalog stats ─────────────────────────────────────────────────────────────
V_stats = V_get_catalog_stats()
st.markdown(f"""
<div class="stats-row">
  <div class="stat-chip">
    <span class="stat-num">{V_stats['total']}</span>
    <span class="stat-label">Total Items</span>
  </div>
  <div class="stat-chip">
    <span class="stat-num">{V_stats['by_media'].get('book', 0)}</span>
    <span class="stat-label">📖 Books</span>
  </div>
  <div class="stat-chip">
    <span class="stat-num">{V_stats['by_media'].get('movie', 0)}</span>
    <span class="stat-label">🎬 Movies</span>
  </div>
  <div class="stat-chip">
    <span class="stat-num">{V_stats['by_media'].get('song', 0)}</span>
    <span class="stat-label">🎵 Songs</span>
  </div>
  <div class="stat-chip">
    <span class="stat-num">EN·IT·HI</span>
    <span class="stat-label">Languages</span>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="yc-divider"></div>', unsafe_allow_html=True)

# ── Main layout ───────────────────────────────────────────────────────────────
S_col_input, S_col_results = st.columns([1, 1.7], gap="large")

with S_col_input:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<p class="yc-section-label">✦ Search Your Item</p>', unsafe_allow_html=True)

    # Build labeled dropdown: "📖 EN · The Great Gatsby"
    V_media_emoji = {"book": "📖", "movie": "🎬", "song": "🎵"}
    V_lang_flag   = {"en": "EN", "it": "IT", "hi": "HI"}
    V_catalog_sorted = sorted(CATALOG, key=lambda V_x: V_x["title"])
    V_dropdown_labels = [
        f"{V_media_emoji[V_item['media']]} {V_lang_flag[V_item['lang']]} · {V_item['title']}"
        for V_item in V_catalog_sorted
    ]
    V_label_to_title = {
        f"{V_media_emoji[V_item['media']]} {V_lang_flag[V_item['lang']]} · {V_item['title']}": V_item["title"]
        for V_item in V_catalog_sorted
    }
    S_selected_label = st.selectbox(
        "Select a title from the catalog",
        options=[""] + V_dropdown_labels,
        index=0,
        key="S_title_select",
        help="📖 = Book · 🎬 = Movie · 🎵 = Song  |  EN / IT / HI = Language"
    )
    S_selected_title = V_label_to_title.get(S_selected_label, "")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p class="yc-section-label">⚙ Filters (optional)</p>', unsafe_allow_html=True)

    S_lang_options = st.multiselect(
        "Languages",
        options=["English (en)", "Italian (it)", "Hindi (hi)"],
        default=[],
        key="S_lang_filter"
    )
    S_lang_map = {
        "English (en)": "en",
        "Italian (it)": "it",
        "Hindi (hi)": "hi",
    }
    S_lang_filter = [S_lang_map[V_l] for V_l in S_lang_options] if S_lang_options else None

    S_media_options = st.multiselect(
        "Media types",
        options=["Books", "Movies", "Songs"],
        default=[],
        key="S_media_filter"
    )
    S_media_map = {"Books": "book", "Movies": "movie", "Songs": "song"}
    S_media_filter = [S_media_map[V_m] for V_m in S_media_options] if S_media_options else None

    S_n_results = st.slider(
        "Number of recommendations",
        min_value=3,
        max_value=8,
        value=4,
        key="S_n_results"
    )

    st.markdown("<br>", unsafe_allow_html=True)
    S_go = st.button("✦  Find My Calling", key="S_go_btn")
    st.markdown('</div>', unsafe_allow_html=True)

    # ── About / How it works ─────────────────────────────────────────────────
    with st.expander("ℹ How YourCalling works"):
        st.markdown("""
        **YourCalling** uses a pure tag-based similarity engine.  
        Every item in the 400-item catalog carries **emotional & thematic tags** — mood, feeling, theme — not genre labels.
        
        **Algorithm:**
        - *60%* — Jaccard overlap of all tags
        - *35%* — Emotional anchor alignment (mood-specific tags)
        - *5%* — Cross-media diversity bonus
        
        **Result:** If a book makes you feel a certain way, YourCalling finds movies and songs that recreate that same emotional space — regardless of plot or genre.
        
        **Catalog:** 130 English books · 70 English movies · 35 Italian movies · 35 Hindi movies · 55 English songs · 35 Italian songs · 40 Hindi songs
        """)


with S_col_results:
    st.markdown('<p class="yc-section-label">✦ Recommendations</p>', unsafe_allow_html=True)

    if S_go and S_selected_title and S_selected_title.strip():
        V_result = V_get_recommendations(
            S_input_title=S_selected_title,
            S_n_results=S_n_results,
            S_lang_filter=S_lang_filter,
            S_media_filter=S_media_filter,
            S_ensure_cross_media=True,
        )

        if V_result["not_found"]:
            st.markdown("""
            <div class="not-found">
              <span>🔍</span>
              No exact match found. Try selecting a title from the dropdown.
            </div>
            """, unsafe_allow_html=True)

        else:
            V_input = V_result["input_item"]
            V_recs  = V_result["recommendations"]

            # ── Input item display ────────────────────────────────────────────
            V_input_icon = V_media_icon(V_input["media"])
            st.markdown(f"""
            <div class="yc-query-card">
              <span class="yc-query-icon">{V_input_icon}</span>
              <div class="yc-query-meta">
                <p class="yc-query-title">{V_input["title"]}</p>
                <p class="yc-query-sub">
                  {V_input["creator"]} &nbsp;·&nbsp;
                  {V_media_label(V_input["media"])} &nbsp;·&nbsp;
                  {V_lang_label(V_input["lang"])}
                </p>
              </div>
            </div>
            """, unsafe_allow_html=True)

            # ── Show input tags ───────────────────────────────────────────────
            V_input_tags_html = "".join(
                f'<span class="tag-pill">{V_t}</span>'
                for V_t in V_input["tags"][:10]
            )
            st.markdown(f"""
            <div style="margin-bottom:1.2rem;">
              <p style="font-size:0.70rem;color:var(--text-muted);letter-spacing:0.1em;
                        text-transform:uppercase;margin-bottom:0.4rem;">Emotional tags</p>
              <div class="tags-row">{V_input_tags_html}</div>
            </div>
            """, unsafe_allow_html=True)

            # ── Recommendation cards ──────────────────────────────────────────
            if not V_recs:
                st.markdown("""
                <div class="not-found">
                  <span>😶</span>
                  No matches found with current filters. Try broadening them.
                </div>
                """, unsafe_allow_html=True)
            else:
                for V_idx, V_entry in enumerate(V_recs, 1):
                    V_item   = V_entry["item"]
                    V_score  = V_entry["score"]
                    V_shared = V_entry["shared_tags"]

                    V_icon       = V_media_icon(V_item["media"])
                    V_media_type = V_item["media"]
                    V_bar_color  = V_score_color(V_score)
                    V_bar_width  = V_score_pct(V_score)

                    # Shared tags (first 6)
                    V_shared_html = "".join(
                        f'<span class="tag-pill shared">{V_t}</span>'
                        for V_t in V_shared[:6]
                    )
                    V_other_tags = [V_t for V_t in V_item["tags"] if V_t not in V_shared]
                    V_other_html = "".join(
                        f'<span class="tag-pill">{V_t}</span>'
                        for V_t in V_other_tags[:4]
                    )

                    st.markdown(f"""
                    <div class="rec-card type-{V_media_type}">
                      <div class="rec-header">
                        <div style="display:flex;align-items:center;gap:0.5rem;">
                          <span style="font-size:1.5rem;">{V_icon}</span>
                          <div>
                            <p class="rec-title">#{V_idx} {V_item["title"]}</p>
                            <p class="rec-creator">{V_item["creator"]}</p>
                          </div>
                        </div>
                        <div style="display:flex;flex-direction:column;align-items:flex-end;gap:0.3rem;">
                          <span class="rec-media-badge badge-{V_media_type}">
                            {V_media_label(V_media_type)}
                          </span>
                          <span class="rec-lang-badge">{V_lang_label(V_item["lang"])}</span>
                        </div>
                      </div>

                      <div class="score-container">
                        <div class="score-label">
                          <span>Emotional Match</span>
                          <span style="color:var(--accent);font-weight:600;">{int(V_score * 200)}%</span>
                        </div>
                        <div class="score-bar-track">
                          <div class="score-bar-fill"
                               style="width:{V_bar_width}%;background:{V_bar_color};"></div>
                        </div>
                      </div>

                      <div class="tags-row">
                        {V_shared_html}
                        {V_other_html}
                      </div>
                      <p style="font-size:0.65rem;color:var(--text-muted);
                                margin-top:0.4rem;letter-spacing:0.05em;">
                        ✦ {len(V_shared)} shared emotional tags
                      </p>
                    </div>
                    """, unsafe_allow_html=True)

    elif S_go and not S_selected_title:
        st.markdown("""
        <div class="not-found">
          <span>👆</span>
          Please select a title first.
        </div>
        """, unsafe_allow_html=True)
    else:
        # ── Idle state ───────────────────────────────────────────────────────
        st.markdown("""
        <div class="glass-card" style="text-align:center;padding:3rem 1.5rem;">
          <p style="font-size:2.5rem;margin:0;">✦</p>
          <p style="font-size:1.05rem;color:var(--text-secondary);margin:0.8rem 0 0.4rem 0;
                    font-weight:500;">Find your emotional match</p>
          <p style="font-size:0.85rem;color:var(--text-muted);max-width:280px;
                    margin:0 auto;line-height:1.6;">
            Select a book, movie, or song and discover
            what else will <em>move you the same way</em> — 
            across all media and languages.
          </p>
        </div>

        <div style="margin-top:1rem;">
          <p class="yc-section-label" style="text-align:center;">Try these</p>
          <div style="display:flex;flex-wrap:wrap;gap:0.4rem;justify-content:center;">
            <span class="tag-pill">The Great Gatsby</span>
            <span class="tag-pill">Cinema Paradiso</span>
            <span class="tag-pill">Tum Hi Ho</span>
            <span class="tag-pill">Norwegian Wood</span>
            <span class="tag-pill">Interstellar</span>
            <span class="tag-pill">Hallelujah</span>
            <span class="tag-pill">Masaan</span>
            <span class="tag-pill">Bella Ciao</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="yc-footer">
  YourCalling · Simran Vishnoi · University of Parma · Data Science for Management<br>
  Pure tag-based similarity · No external APIs · 400 items across Books · Movies · Songs
</div>
""", unsafe_allow_html=True)
