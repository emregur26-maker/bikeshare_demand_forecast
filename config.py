from pathlib import Path

PROJECT_ROOT: Path = Path(__file__).resolve().parent
DATA_DIR: Path = PROJECT_ROOT / "data"
RAW_DIR: Path = DATA_DIR / "raw"
INTERIM_DIR: Path = DATA_DIR / "interim"
PROCESSED_DIR: Path = DATA_DIR / "processed"
RESULTS_DIR: Path = PROJECT_ROOT / "results"
DIRS_TO_CREATE: tuple[Path, ...] = (
    DATA_DIR,
    RAW_DIR,
    INTERIM_DIR,
    PROCESSED_DIR,
    RESULTS_DIR,
)

DATA_SOURCE_URL: str = (
    "https://s3.amazonaws.com/capitalbikeshare-data/"
    "{month_compact}-capitalbikeshare-tripdata.zip"
)
MONTHS: tuple[str, ...] = ("2025-01", "2025-02", "2025-03")
SAMPLE_ROWS: int | None = 50_000
TARGET_FREQ: str = "h"
FORECAST_HORIZON_HOURS: int = 24
RANDOM_SEED: int = 42
LOG_LEVEL: str = "INFO"
