# The Briefing

Official morning paper for the NBFC jobs. This design is final.

## Open it

Double-click:

`C:\Users\gopal\NBFC Briefing\reader.html`

Or open that file in Hermes preview.

## How to read it

- **News** — Daily Watch (jarvis, 7:00 AM)
- **Rules** — Regulatory Monitor (NBFC Guru, 8:15 AM)
- **Weekly** — Weekly Analysis (jarvis, Mondays 7:15 AM)

Pick a date in the top bar. Tap a desk that says *Ready to read*. The article is on the page.

## What files where

```
reader.html     the paper
publish.py      rebuilds the index after a job files
data.js         generated — do not edit by hand
days/YYYY-MM-DD/
  01-daily-watch.md
  02-regulation.md
  03-weekly-analysis.md   Mondays only
demo/           old sketches, not the product
```

Jobs write the markdown themselves, then run `python publish.py`.
