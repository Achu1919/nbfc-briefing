#!/usr/bin/env bash
# nbfc-briefing deploy — wrapper around the canonical Python deploy script.
#
# The real implementation lives at:
#   C:/Users/gopal/AppData/Local/hermes/profiles/jarvis/scripts/nbfc-deploy.py
# It is what the "NBFC Deploy to Vercel" cron job (jarvis profile, 9:00 AM IST) runs.
# Logic is Python because cron .sh jobs on Windows route through `shutil.which("bash")`,
# which can hit C:\Windows\System32\bash.exe (the WSL stub) and fail.
# This wrapper is only for manual runs from a Git Bash console.
set -euo pipefail
exec python "C:/Users/gopal/AppData/Local/hermes/profiles/jarvis/scripts/nbfc-deploy.py"
