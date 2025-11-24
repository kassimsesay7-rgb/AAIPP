'''Task Description #1
Use Google Gemini in Colab to write a function that reads a CSV file 
and calculates mean, min, max.'''


from __future__ import annotations

import csv
from typing import Dict, List, Optional, Union


def read_csv_and_stats(
    filepath: str,
    column: Optional[str] = None,
) -> Union[Dict[str, Dict[str, float]], Dict[str, float]]:
    """
    Read a CSV file and compute mean, min, and max for numeric data.

    If `column` is provided, returns a dict with keys 'mean', 'min', 'max' for that column.
    Otherwise returns a mapping for each numeric column to its stats.
    Non-numeric values are ignored.
    """

    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV file has no header row.")

        numeric_values_by_column: Dict[str, List[float]] = {name: [] for name in reader.fieldnames}

        for row in reader:
            for name, value in row.items():
                if value is None or value == "":
                    continue
                try:
                    numeric_values_by_column[name].append(float(value))
                except (TypeError, ValueError):
                    # Ignore non-numeric values
                    pass

        def stats(values: List[float]) -> Dict[str, float]:
            if not values:
                raise ValueError("No numeric data found for requested column.")
            return {
                "mean": sum(values) / len(values),
                "min": min(values),
                "max": max(values),
            }

        if column is not None:
            if column not in numeric_values_by_column:
                raise KeyError(f"Column '{column}' not found in CSV header.")
            return stats(numeric_values_by_column[column])

        result: Dict[str, Dict[str, float]] = {}
        for name, values in numeric_values_by_column.items():
            if values:
                result[name] = stats(values)
        return result


if __name__ == "__main__":
    # Example usage: change the path or column name as needed
    path = "sample_data.csv"
    all_stats = read_csv_and_stats(path)
    print("All numeric columns:", all_stats)
    # Example for a specific column (uncomment and set an existing column name):
    # print(read_csv_and_stats(path, column="your_numeric_column"))


