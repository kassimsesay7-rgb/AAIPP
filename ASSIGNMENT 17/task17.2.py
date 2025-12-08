print("\n==================== TASK 2: FINANCIAL DATA ====================")

import pandas as pd
import numpy as np

financial_df = pd.read_csv("financial_data.csv")

# BEFORE SUMMARY
print("\n--- BEFORE ---")
print(financial_df.head())

# Missing values
financial_df["closing_price"] = financial_df["closing_price"].fillna(method="ffill")
financial_df["volume"] = financial_df["volume"].fillna(financial_df["volume"].median())

# Lag features
financial_df["return_1d"] = financial_df["closing_price"].pct_change()
financial_df["return_7d"] = financial_df["closing_price"].pct_change(periods=7)

# Log normalize volume
financial_df["volume_log"] = np.log1p(financial_df["volume"])

# Outlier detection (IQR)
Q1 = financial_df["closing_price"].quantile(0.25)
Q3 = financial_df["closing_price"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

financial_df = financial_df[(financial_df["closing_price"] >= lower) &
                            (financial_df["closing_price"] <= upper)]

# AFTER SUMMARY
print("\n--- AFTER ---")
print(financial_df.head())

# TESTS
assert financial_df["volume"].isna().sum() == 0
assert "return_1d" in financial_df.columns
assert financial_df["volume_log"].min() >= 0

print("\nTask 2 Passed All Tests ✔")

