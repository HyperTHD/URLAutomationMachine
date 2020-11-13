#!/bin/bash

set -e

if [ $# -eq 0 ]; then
    # Default (if no args provided).
    sh -c "python -m pylint urlChecker.py urlClass.py"
else
    # Custom args.
    sh -c "python -m pylint $*"
fi