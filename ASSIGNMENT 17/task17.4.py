"""
Task 17.4 – Real-Time Application: Movie Reviews Data Cleaning

Goal
-----
Prepare a movie reviews dataset for downstream **sentiment classification** by:
- Standardising review text (lowercasing, removing HTML tags).
- Tokenising and encoding reviews using TF–IDF.
- Handling missing ratings via median imputation.
- Normalising numeric ratings from a 0–10 scale to a 0–1 scale.
- Generating a simple before/after summary report.

------------------------------------------------------------------
AI-GENERATED PROMPTS (for your written report)
------------------------------------------------------------------
Code generation prompt
~~~~~~~~~~~~~~~~~~~~~~
    "Write a Python script that reads a CSV of movie reviews with
    columns review_id, review_text, rating and performs the following:
    - lowercases review_text and removes HTML tags,
    - fills missing ratings with the median rating,
    - normalizes ratings from a 0–10 scale to 0–1,
    - encodes the cleaned text using TF-IDF,
    - prints a small before/after text cleaning summary and saves a
      cleaned CSV ready for sentiment classification."

Test generation prompt
~~~~~~~~~~~~~~~~~~~~~~
    "Given the movie review cleaning script, generate at least three
    assert-style tests that check:
    - HTML is removed and text is lowercased correctly,
    - missing ratings are imputed with the column median,
    - normalized ratings lie in the [0, 1] range and match rating/10,
    - TF-IDF encoding produces a non-empty vocabulary."
"""

import re

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def clean_html(text: str) -> str:
    """Lowercase and remove HTML tags from review text."""
    if not isinstance(text, str):
        return ""
    text = text.lower()
    # Remove any simple HTML-like tags such as <p>, <br>, etc.
    text = re.sub(r"<.*?>", "", text)
    # Collapse extra whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


def preprocess_reviews(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply the full preprocessing steps on the movie_reviews DataFrame.

    - Clean and standardise text into `clean_text`.
    - Fill missing ratings with the median (`rating_filled`).
    - Normalise ratings to [0, 1] (`rating_norm`).
    """
    df = df.copy()

    # 1. Clean and standardise text
    df["clean_text"] = df["review_text"].apply(clean_html)

    # 2. Handle missing ratings via median
    median_rating = df["rating"].median()
    df["rating_filled"] = df["rating"].fillna(median_rating)

    # 3. Normalise ratings 0–10 → 0–1
    df["rating_norm"] = df["rating_filled"] / 10.0

    return df


def encode_tfidf(df: pd.DataFrame) -> tuple[TfidfVectorizer, np.ndarray]:
    """Tokenise + encode cleaned text using TF–IDF."""
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(df["clean_text"])
    return vectorizer, tfidf_matrix


def print_before_after_summary(df_raw: pd.DataFrame, df_clean: pd.DataFrame) -> None:
    """Print a small before vs after text summary."""
    summary_report = pd.DataFrame(
        {
            "before_cleaning": df_raw["review_text"].head(),
            "after_cleaning": df_clean["clean_text"].head(),
        }
    )

    print("\n--- BEFORE vs AFTER CLEANING ---")
    print(summary_report)


# ------------------------------
# Simple assert-style test cases
# ------------------------------

def _test_clean_html() -> None:
    """Check that HTML is removed and text is lowercased."""
    raw = "<p>Amazing Movie!</p>"
    cleaned = clean_html(raw)
    assert "<p>" not in cleaned and "</p>" not in cleaned, "HTML tags should be removed."
    assert cleaned == "amazing movie!", "Text should be fully lowercased."


def _test_missing_and_normalized_ratings() -> None:
    """Check median imputation and 0–1 normalisation."""
    df = pd.DataFrame(
        {
            "review_id": [1, 2, 3],
            "review_text": ["a", "b", "c"],
            "rating": [8.0, np.nan, 4.0],
        }
    )
    df_prep = preprocess_reviews(df)
    # Median of [8, 4] is 6
    assert df_prep["rating_filled"].iloc[1] == 6.0, "Missing rating should be filled with median."

    expected_norm = df_prep["rating_filled"] / 10.0
    assert np.allclose(
        df_prep["rating_norm"], expected_norm
    ), "Normalized rating must equal rating_filled / 10."
    assert df_prep["rating_norm"].between(0.0, 1.0).all(), "Normalized ratings must lie in [0, 1]."


def _test_tfidf_encoding() -> None:
    """Check that TF–IDF encoding works and vocabulary is non-empty."""
    df = pd.DataFrame(
        {
            "review_id": [1, 2],
            "review_text": ["Great movie", "Bad plot"],
            "rating": [8.0, 2.0],
        }
    )
    df_prep = preprocess_reviews(df)
    vectorizer, tfidf_matrix = encode_tfidf(df_prep)

    vocab = vectorizer.vocabulary_
    assert "great" in vocab and "bad" in vocab, "Expected tokens should be in vocabulary."
    assert tfidf_matrix.shape[0] == 2, "TF–IDF rows must match number of reviews."
    assert tfidf_matrix.shape[1] == len(vocab), "Columns should match vocabulary size."


def run_tests() -> None:
    """Run all simple assert-based tests for Task 17.4."""
    _test_clean_html()
    _test_missing_and_normalized_ratings()
    _test_tfidf_encoding()
    print("All Task 17.4 tests passed.")


if __name__ == "__main__":
    # Load dataset
    raw_df = pd.read_csv("movie_reviews-1.csv")

    # Apply preprocessing steps
    cleaned_df = preprocess_reviews(raw_df)

    # Encode reviews using TF–IDF (features kept in memory for modelling)
    tfidf_vectorizer, tfidf_features = encode_tfidf(cleaned_df)

    # Print a before vs after text cleaning summary
    print_before_after_summary(raw_df, cleaned_df)

    # Save cleaned dataset ready for sentiment classification
    cleaned_df.to_csv("movie_reviews_cleaned.csv", index=False)
    print("\nCleaning Completed Successfully! Saved to movie_reviews_cleaned.csv")

    # Run local tests and report result
    run_tests()
