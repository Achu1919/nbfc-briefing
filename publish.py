from __future__ import annotations

import json
import re
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DAYS = ROOT / "days"
OUT = ROOT / "data.js"

JOBS = {
    "01-daily-watch": {
        "section": "News",
        "kind": "Daily Watch",
        "agent": "jarvis",
        "when": "7:00 AM",
        "question": "What happened in markets and the sector?",
        "monday_only": False,
    },
    "02-regulation": {
        "section": "Rules",
        "kind": "Regulation",
        "agent": "NBFC Guru",
        "when": "8:15 AM",
        "question": "What changed in the rulebook?",
        "monday_only": False,
    },
    "03-weekly-analysis": {
        "section": "Weekly",
        "kind": "Weekly Analysis",
        "agent": "jarvis",
        "when": "7:15 AM Mondays",
        "question": "What did the whole week mean?",
        "monday_only": True,
    },
}


def clean_inline(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"[*_`#]", "", value)
    return re.sub(r"\s+", " ", value).strip()


def first_heading(text: str, fallback: str) -> str:
    for line in text.splitlines():
        match = re.match(r"^#{1,3}\s+(.+?)\s*$", line)
        if match:
            heading = clean_inline(match.group(1))
            if "Daily Watch" in heading:
                return "News and markets"
            if "Regulatory Daily Report" in heading or "NBFC Guru" in heading:
                return "What changed in the rules"
            if "Weekly Analysis" in heading:
                return "The week in NBFCs"
            return heading
    return fallback


def excerpt(text: str) -> str:
    for block in re.split(r"\n\s*\n", text):
        block = block.strip()
        if not block or block.startswith("#") or block.startswith("---"):
            continue
        lines = [
            line
            for line in block.splitlines()
            if not line.lstrip().startswith(("|", "- ", "* "))
        ]
        if lines:
            return clean_inline(" ".join(lines))[:220]
    return ""


def read_report(path: Path, key: str, folder: str) -> dict:
    text = path.read_text(encoding="utf-8")
    meta = JOBS[key]
    return {
        "id": f"{folder}-{key}",
        "key": key,
        "section": meta["section"],
        "kind": meta["kind"],
        "agent": meta["agent"],
        "when": meta["when"],
        "question": meta["question"],
        "monday_only": meta["monday_only"],
        "title": first_heading(text, meta["kind"]),
        "excerpt": excerpt(text),
        "content": text,
        "missing": False,
        "expected": True,
        "file": path.name,
    }


def empty_report(key: str, folder: str, expected: bool) -> dict:
    meta = JOBS[key]
    if not expected:
        title = "Not due today"
        excerpt_text = "This job only files on Mondays."
    else:
        title = "Did not arrive"
        excerpt_text = f"The {meta['when']} job did not leave a file."
    return {
        "id": f"{folder}-{key}",
        "key": key,
        "section": meta["section"],
        "kind": meta["kind"],
        "agent": meta["agent"],
        "when": meta["when"],
        "question": meta["question"],
        "monday_only": meta["monday_only"],
        "title": title,
        "excerpt": excerpt_text,
        "content": "",
        "missing": True,
        "expected": expected,
        "file": f"{key}.md",
    }


def build() -> dict:
    days = []
    DAYS.mkdir(parents=True, exist_ok=True)
    windows = __import__("sys").platform.startswith("win")
    for day_dir in sorted((p for p in DAYS.iterdir() if p.is_dir()), reverse=True):
        try:
            day = date.fromisoformat(day_dir.name)
        except ValueError:
            continue
        is_monday = day.weekday() == 0
        reports = []
        for key, meta in JOBS.items():
            path = day_dir / f"{key}.md"
            expected = (not meta["monday_only"]) or is_monday
            if path.exists():
                reports.append(read_report(path, key, day_dir.name))
            else:
                reports.append(empty_report(key, day_dir.name, expected))
        days.append(
            {
                "id": day_dir.name,
                "label": day.strftime("%A, %#d %B %Y") if windows else day.strftime("%A, %-d %B %Y"),
                "iso": day_dir.name,
                "weekday": day.strftime("%A"),
                "is_monday": is_monday,
                "reports": reports,
            }
        )
    return {"generated": datetime.now().isoformat(timespec="seconds"), "days": days}


if __name__ == "__main__":
    payload = build()
    OUT.write_text(
        "window.BRIEFING = " + json.dumps(payload, ensure_ascii=False) + ";\n",
        encoding="utf-8",
    )
    print(f"Published {len(payload['days'])} day(s) to {OUT}")
