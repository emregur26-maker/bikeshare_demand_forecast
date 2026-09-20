from pathlib import Path

import config


def project_root() -> Path:
    return config.PROJECT_ROOT


def ensure_dirs() -> None:
    for directory in config.DIRS_TO_CREATE:
        directory.mkdir(parents=True, exist_ok=True)
