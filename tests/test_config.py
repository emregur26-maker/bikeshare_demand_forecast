from pathlib import Path

import config
from common import paths

REQUIRED_NAMES = (
    "PROJECT_ROOT",
    "DATA_DIR",
    "RAW_DIR",
    "INTERIM_DIR",
    "PROCESSED_DIR",
    "RESULTS_DIR",
    "DIRS_TO_CREATE",
    "DATA_SOURCE_URL",
    "MONTHS",
    "SAMPLE_ROWS",
    "TARGET_FREQ",
    "FORECAST_HORIZON_HOURS",
    "RANDOM_SEED",
    "LOG_LEVEL",
)


def test_interface_names_exist():
    for name in REQUIRED_NAMES:
        assert hasattr(config, name), f"config.{name} is missing"


def test_paths_are_inside_project_root():
    path_names = ("DATA_DIR", "RAW_DIR", "INTERIM_DIR", "PROCESSED_DIR", "RESULTS_DIR")
    for name in path_names:
        path: Path = getattr(config, name)
        assert config.PROJECT_ROOT in path.parents


def test_dirs_to_create_has_five_entries():
    assert len(config.DIRS_TO_CREATE) == 5


def test_ensure_dirs_is_idempotent():
    paths.ensure_dirs()
    paths.ensure_dirs()
    for directory in config.DIRS_TO_CREATE:
        assert directory.exists()
