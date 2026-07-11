# YourCalling

A cross-media recommendation engine: give it a book, movie or song you love and it suggests things to read, watch and listen to that share the same emotional feel. Built with Streamlit, no external APIs.

Most recommenders stay inside one medium (Spotify suggests songs, Goodreads suggests books). The idea here is that what people actually chase is a mood, and moods cross media. If you loved *Norwegian Wood*, you might want a melancholic film, not another Murakami novel.

## How it works

Every item in the catalog (`data/catalog.py`) is hand-tagged with themes, moods and style tags. The engine (`engine/similarity.py`) scores similarity as:

- 60% Jaccard overlap of all tags
- 35% overlap of "emotional anchor" tags (melancholic, hopeful, haunting, etc.)
- a small bonus when the recommendation is a different media type, so results stay cross-media

Scores are transparent: the UI shows which shared tags drove each recommendation.

## Run it

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Limitations

The catalog is small and hand-curated, so coverage is limited, and tag-based matching only works as well as the tagging. This was mainly an exercise in building a recommender without embeddings or APIs and keeping the scoring explainable.

## Author

Simran Vishnoi — MSc Data Science for Management, University of Parma
