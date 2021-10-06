#!/usr/bin/env python
"""Launch a shell to start Django development server. Require Python 3.5+ installed."""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
TARGET = BASE_DIR.joinpath("manage.py")
COMMAND = "runserver"

if __name__ == "__main__":
    os.system(f"{TARGET} {COMMAND}")
