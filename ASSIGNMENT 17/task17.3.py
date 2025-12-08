"""
Task 17.3 – IoT Sensor Data Preparation

Clean and preprocess IoT temperature and humidity logs for anomaly detection.

Steps:
- Handle missing values using forward fill (per sensor, time-ordered).
- Remove sensor drift via rolling mean smoothing.
- Normalize numeric readings using standard scaling.
- Encode categorical sensor IDs.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder


RAW_DATA_PATH = Path("iot_sensor.csv")
PREPARED_DATA_PATH = Path("iot_sensor_prepared.csv")


def load_iot_data(path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """Load the raw IoT sensor CSV and parse timestamps."""
    df = pd.read_csv(path)
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    # Ensure deterministic ordering for time-based operations
    df = df.sort_values(["sensor_id", "timestamp"]).reset_index(drop=True)
    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing temperature / humidity using forward fill within each sensor.

    If the first value for a sensor is missing, a backward fill is applied as a
    secondary step so no gaps remain in the series.
    """
    df = df.copy()
    for col in ["temperature", "humidity"]:
        if col not in df:
            continue
        df[col] = (
            df.groupby("sensor_id")[col]
            .apply(lambda s: s.ffill().bfill())
            .reset_index(level=0, drop=True)
        )
    return df


def apply_rolling_mean(df: pd.DataFrame, window: int = 3) -> pd.DataFrame:
    """
    Smooth readings with a rolling mean to reduce sensor drift/noise.

    Uses a small centred window per sensor. For edge points where the full
    window is not available, fewer points are used (min_periods=1).
    """
    df = df.copy()
    for col in ["temperature", "humidity"]:
        if col not in df:
            continue
        rolled = (
            df.groupby("sensor_id")[col]
            .rolling(window=window, min_periods=1, center=True)
            .mean()
            .reset_index(level=0, drop=True)
        )
        df[f"{col}_smoothed"] = rolled
    return df


def encode_sensor_ids(df: pd.DataFrame) -> pd.DataFrame:
    """Encode the categorical sensor_id column using label encoding."""
    df = df.copy()
    encoder = LabelEncoder()
    df["sensor_id_encoded"] = encoder.fit_transform(df["sensor_id"].astype(str))
    return df


def scale_numeric_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standard-scale numeric readings for anomaly detection.

    The scaler is fit on the current dataset and applied column-wise.
    """
    df = df.copy()
    numeric_cols = [
        col
        for col in ["temperature", "humidity", "temperature_smoothed", "humidity_smoothed"]
        if col in df.columns
    ]
    if not numeric_cols:
        return df

    scaler = StandardScaler()
    scaled_values = scaler.fit_transform(df[numeric_cols])
    for i, col in enumerate(numeric_cols):
        df[f"{col}_scaled"] = scaled_values[:, i]
    return df


def prepare_iot_dataset(
    input_path: Path = RAW_DATA_PATH,
    output_path: Path = PREPARED_DATA_PATH,
) -> pd.DataFrame:
    """Full preprocessing pipeline for IoT temperature and humidity logs."""
    df = load_iot_data(input_path)
    df = handle_missing_values(df)
    df = apply_rolling_mean(df, window=3)
    df = encode_sensor_ids(df)
    df = scale_numeric_features(df)

    # Reorder columns for clarity in downstream anomaly detection
    desired_order = [
        "timestamp",
        "sensor_id",
        "sensor_id_encoded",
        "temperature",
        "humidity",
        "temperature_smoothed",
        "humidity_smoothed",
        "temperature_scaled",
        "humidity_scaled",
        "temperature_smoothed_scaled",
        "humidity_smoothed_scaled",
    ]

    # Keep only columns that exist, in the specified order, plus any extras
    ordered_cols = [c for c in desired_order if c in df.columns]
    remaining_cols = [c for c in df.columns if c not in ordered_cols]
    df = df[ordered_cols + remaining_cols]

    df.to_csv(output_path, index=False)
    return df


if __name__ == "__main__":
    prepared = prepare_iot_dataset()
    print("Prepared IoT dataset saved to:", PREPARED_DATA_PATH.resolve())
    print(prepared.head())


