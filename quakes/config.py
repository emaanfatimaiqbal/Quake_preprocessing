from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FALLBACK_PATH = ROOT / "data" / "fallback" / "all_week.geojson"
STREAM_DIR = ROOT / "data" / "stream"
PROCESSED_DIR = ROOT / "data" / "processed"

SEED = 42
TARGET = "big_quake"

# TODO (Task 4 and 5): fill these in after you have explored the data.
# NUMERIC: list[str] = [
NUMERIC = [
    "nst",
    "update_lag_hours",
    "lat",
    "lon",
    "depth_km",
    ]   # numeric feature columns
NOMINAL = [
    "status",
    ]   # categorical feature columns (one-hot encoded)
# LEAKY: list[str] = [
#     "title",
#     "sig",
#     "mmi",
#     "cdi",
#     "felt",
#     "alert",]     # columns that encode the magnitude: must be dropped
