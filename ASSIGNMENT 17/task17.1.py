"""
Task 17.1 – Social Media Data Cleaning

Reads the raw dataset, normalizes the text field, imputes missing engagement
metrics, enriches timestamps with structured temporal features, and removes spam
duplication. Produces a cleaned CSV ready for downstream analysis.
"""

from __future__ import annotations

import re
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


RAW_DATA_PATH = Path("social_media (1).csv")
CLEAN_DATA_PATH = Path("cleaned_social_media.csv")

# Lightweight stopword extension to strip obvious noise terms from this dataset.
STOPWORDS = set(ENGLISH_STOP_WORDS).union(
    {
        "html",
        "post",
        "sample",
    }
)


def clean_post_text(text: str) -> str:
    """Lowercase, strip markup/symbols, remove stopwords."""
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = re.sub(r"<[^>]+>", " ", text)  # remove HTML-like tags
    text = re.sub(r"[^a-z0-9\s]", " ", text)  # keep alphanumerics
    tokens = [token for token in text.split() if token and token not in STOPWORDS]
    return " ".join(tokens)


def handle_missing_engagement(df: pd.DataFrame) -> pd.DataFrame:
    """Fill likes/shares with their respective medians."""
    for column in ("likes", "shares"):
        if column in df:
            median_value = df[column].median()
            df[column] = df[column].fillna(median_value)
    return df


def enrich_timestamp(df: pd.DataFrame) -> pd.DataFrame:
    """Convert timestamp to datetime and derive hour/weekday."""
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df["hour"] = df["timestamp"].dt.hour
    df["weekday"] = df["timestamp"].dt.day_name()
    return df


def remove_spam_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Drop duplicate posts based on the cleaned text value."""
    df = df.copy()
    df["post_text_clean"] = df["post_text"].apply(clean_post_text)
    df = df[df["post_text_clean"] != ""]
    df = df.drop_duplicates(subset="post_text_clean", keep="first")
    return df


def clean_social_media_dataset(
    input_path: Path = RAW_DATA_PATH,
    output_path: Path = CLEAN_DATA_PATH,
) -> pd.DataFrame:
    """Full cleaning pipeline."""
    df = pd.read_csv(input_path)
    df = handle_missing_engagement(df)
    df = enrich_timestamp(df)
    df = remove_spam_duplicates(df)
    df = df[
        [
            "post_id",
            "user",
            "post_text",
            "post_text_clean",
            "likes",
            "shares",
            "timestamp",
            "hour",
            "weekday",
        ]
    ]
    df.to_csv(output_path, index=False)
    return df


if __name__ == "__main__":
    cleaned = clean_social_media_dataset()
    print("Cleaned dataset saved to:", CLEAN_DATA_PATH.resolve())
    print(cleaned.head())

