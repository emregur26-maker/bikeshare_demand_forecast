import argparse
import logging

import config
from common import paths

logger = logging.getLogger(__name__)


def _run_check(args: argparse.Namespace) -> int:
    logging.basicConfig(level=config.LOG_LEVEL)
    paths.ensure_dirs()
    for directory in config.DIRS_TO_CREATE:
        logger.info("%s exists=%s", directory, directory.exists())
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="run.py")
    subparsers = parser.add_subparsers(dest="command", required=True)

    check_parser = subparsers.add_parser("check", help="verify the environment and data directories")
    check_parser.set_defaults(func=_run_check)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
