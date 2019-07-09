#!/usr/bin/env bash
source /Users/swithana/git/komadu/GrayScott/komadu_venv/bin/activate
RUN_DIR=$PWD
cd /Users/swithana/git/komadu/GrayScott
python3 komadu_client/main.py --static $RUN_DIR