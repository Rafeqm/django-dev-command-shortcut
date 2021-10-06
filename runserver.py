#!/usr/bin/env python
"""Run python command to start Django development server.  Require Python 3.5+
installed."""

import sys
import os
from pathlib import Path

PYTHON_INTERPRETER = "python" if sys.platform.startswith("win") else "python3"
BASE_DIR = Path(__file__).resolve().parent
TARGET = BASE_DIR.joinpath("manage.py")
COMMAND = "runserver"

if __name__ == "__main__":
    os.system(f"{PYTHON_INTERPRETER} {TARGET} {COMMAND}")
