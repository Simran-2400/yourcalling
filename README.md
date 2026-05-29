# YourCalling 🎵📖🎬
**Cross-Media Recommendation Engine**  
Simran Vishnoi · University of Parma · Data Science for Management

---

## What it does
Input any **book, movie, or song** from the 400-item catalog and receive 3–4 recommendations **across all three media** based on **emotional essence, mood, and theme matching** — not genre or plot.

## Catalog
| Media | Language | Count |
|-------|----------|-------|
| Books | English | 130 |
| Movies | English | 70 |
| Movies | Italian | 35 |
| Movies | Hindi | 35 |
| Songs | English | 55 |
| Songs | Italian | 35 |
| Songs | Hindi | 40 |
| **Total** | | **400** |

## Algorithm
Pure tag-based Jaccard similarity. No APIs required.
- **60%** — Jaccard tag overlap (all tags)
- **35%** — Emotional anchor alignment (mood-specific tags)
- **5%** — Cross-media diversity bonus

---

## Setup on Mac

```bash
# 1. Navigate to project folder (drag folder into Terminal or:)
cd ~/Desktop/yourcalling    # adjust path as needed

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

The app opens automatically at **http://localhost:8501**

---

## Project Structure
```
yourcalling/
├── app.py                  ← Main Streamlit app (dark glassmorphism UI)
├── requirements.txt
├── README.md
├── data/
│   ├── __init__.py
│   └── catalog.py          ← 400-item catalog with emotional tags
└── engine/
    ├── __init__.py
    └── similarity.py       ← Jaccard similarity + weighted scoring engine
```

---

## Variable naming convention
- `S_` prefix → input variables
- `V_` prefix → computed/derived variables
