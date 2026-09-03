#!/usr/bin/env bash
# nbfc-briefing deploy: rebuild data.js, commit, push to GitHub
# Vercel auto-deploys from the GitHub push.
set -euo pipefail

REPO="C:/Users/gopal/NBFC Briefing"
cd "$REPO"

echo "=== Rebuilding data.js ==="
python publish.py

echo "=== Git status ==="
git add -A
CHANGES=$(git diff --cached --stat)
if [ -z "$CHANGES" ]; then
  echo "No changes to commit. Done."
  exit 0
fi

TODAY=$(date +%Y-%m-%d)
git commit -m "daily: update briefing for $TODAY"
git push origin master
echo "=== Pushed to GitHub. Vercel will auto-deploy. ==="
