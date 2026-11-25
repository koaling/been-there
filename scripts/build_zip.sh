#!/bin/sh
# Rebuilds dist/been-there.zip (the skill package people upload to Claude).
set -e
cd "$(dirname "$0")/.."
rm -f dist/been-there.zip
# -X and a fixed timestamp keep the ZIP identical when nothing changed
find been-there -exec touch -t 202001010000 {} +
zip -rqX dist/been-there.zip been-there -x "been-there/.claude-plugin/*"
echo "Built dist/been-there.zip"
