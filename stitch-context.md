# The Briefing — Redesign Context for Stitch (Google)

Copy-paste the block under "PASTE INTO STITCH" into Stitch. This file is the full version with technical appendix.

---

## PASTE INTO STITCH

**Project: Redesign "The Briefing" — a private daily NBFC intelligence site**

I want a full design for a redesign of my existing private briefing site "The Briefing". It is a single-user, mobile + desktop, editorial reading site. Think "private morning newspaper for one finance professional". Design 3 screens: (1) Home / Today view, (2) Article reading view, (3) Archive / Search view. Include mobile and desktop layouts, plus Morning (light) and Evening (dark) modes.

**Who it is for:**
One reader — Achu (Sai Krishna), FP&A at Muthoot Fincorp HO, India. He reads every morning on phone (~7–9 AM IST) and sometimes on desktop. He is NOT a coder. He wants to scan in 2 minutes and deep-dive in 15 minutes. All content is about Indian NBFCs / lending / gold loans / RBI regulation.

**What the site does today (you must keep all of this):**
1. Daily edition grouped by date (e.g. "Friday, 4 September 2026"). A date picker switches days, newest first.
2. Each day has 2–3 "desks" (report cards):
   - NEWS / Daily Watch by jarvis, 7:00 AM — "What happened in markets and the sector?"
   - RULES / Regulation by NBFC Guru, 8:15 AM — "What changed in the rulebook?"
   - WEEKLY / Weekly Analysis by jarvis, Mondays 7:15 AM only — "What did the whole week mean?"
   - Each card shows: section tag, one-line question, agent + time + status. Status is either "Ready to read", "Did not file" (job failed), or "Monday only" (not due). Failed/Monday cards are disabled, not clickable.
3. Clicking a desk opens the article sheet: department eyebrow label, big serif headline, byline (kind · agent · time · date), italic lede/excerpt summary, then the full markdown body.
4. Body content includes: urgent/high-impact lead stories, market & stock summary (Sensex/Nifty/FII-DII/gold), RBI headlines, results, rating actions, deals, digital/fintech, NPA/asset quality, personnel moves, a rotating Friday sector deep-dive (e.g. Auto & EV lending), penalty tables, pipeline trackers, and 30–45 numbered source links (must open in new tab).
5. Markdown features to support: H1/H2/H3, bold, italic, bullet lists, horizontal rules, data tables (must look good on mobile), inline links, drop-cap on first paragraph, pull-style lede.
6. Morning/Evening mode toggle, remembered across visits.
7. Fully static site on Vercel, no login, no backend, no comments. Fast load, readable typography.

**New features I want in the redesign (design for these):**
1. Today hero: date, "2-minute scan" urgent top-3 strip + market snapshot strip (Sensex/Nifty, gold price, FII/DII).
2. Desk cards with visual hierarchy — urgent items flagged, reading-time estimate, unread state.
3. Article view with sticky mini-nav / table of contents (Urgent, Markets, RBI, Results, Ratings, Deals, Digital, NPA, People, Deep dive, Sources), back-to-top, prev/next desk, share-copy-link.
4. Audio briefing player bar (daily podcast script exists — design a play bar with transcript toggle).
5. Archive view: calendar + list of past days with status dots (filed/missing), search across all headlines and body, filter by desk (News/Rules/Weekly) and by topic tags.
6. "Muthoot lens" callout component: a highlighted box for "why this matters for Muthoot Fincorp" inside articles.
7. Source-links section designed as a clean numbered reference list, tappable on mobile.
8. Empty states: "Did not arrive" and "Not due today (Monday only)".

**Style direction: Liquid Glass × Material 3 Expressive mix.**
Fuse Apple's Liquid Glass with Google's Material 3 (M3 Expressive): frosted liquid-glass surfaces (translucent, blurred, subtle specular edge-light, soft depth) APPLIED to M3 structure and components. Use M3's tonal color system + dynamic color (morning = light tonal palette with blue seed #0071e3; evening = dark tonal palette with blue #2997ff), large rounded shapes (16–28px cards/sheets), M3 type scale (big serif display headlines allowed — Newsreader for article headlines, M3 sans e.g. Roboto/Google Sans for UI labels), state layers on press/hover, and real M3 components: bottom navigation bar (Today / Archive / Search), segmented buttons for desk switching (News / Rules / Weekly), M3 search bar + filter chips in Archive, cards with tonal fills + glass blur over gradient, FAB / extended FAB for the audio briefing player, switch for Morning/Evening mode, snackbars for "link copied". Mobile-first, 44px+ touch targets, accessible (focus states, reduced-motion + reduced-transparency fallbacks, contrast). No clutter, no ads, no paywall UI. Feel: premium fintech newspaper that feels native on both iPhone and Android.

**Do NOT include:** login/signup, multi-user, comments, notifications settings pages, ads, paywall, charts dashboard (simple snapshot strip only).

**Deliverables I expect from you:** the 3 screens above in light + dark, mobile + desktop, with realistic sample content from an NBFC morning (gold-loan LTV pressure, RBI revolving-credit rethink, ARCIL IPO, Sensex/Nifty close, rating upgrades). Use the content structure above so the design fits real data.

---

## APPENDIX (for fidelity — do not paste unless Stitch asks)

**Live site:** https://nbfc-briefing.vercel.app/ and /reader.html
**Repo:** GitHub Achu1919/nbfc-briefing. Local folder: `C:\Users\gopal\NBFC Briefing`
**Stack:** static `index.html` + `reader.html` + `data.js` (generated), hosted with `@vercel/static`. Routes: `/` → index.html, `/reader` → reader.html.
**Pipeline:** `days/YYYY-MM-DD/01-daily-watch.md`, `02-regulation.md`, `03-weekly-analysis.md` (Mondays only), `podcast-script.txt` → `publish.py` builds `window.BRIEFING = {generated, days[]}` → `deploy.sh` commits + pushes, Vercel auto-deploys.

**Data model (data.js):**
```js
window.BRIEFING = {
  generated: "2026-09-04T08:42:29",
  days: [{
    id: "2026-09-04", label: "Friday, 4 September 2026",
    iso: "2026-09-04", weekday: "Friday", is_monday: false,
    reports: [{
      id: "2026-09-04-01-daily-watch", key: "01-daily-watch",
      section: "News", kind: "Daily Watch", agent: "jarvis", when: "7:00 AM",
      question: "What happened in markets and the sector?",
      monday_only: false, title: "News and markets",
      excerpt: "Morning edition: ...",
      content: "# markdown source...",
      missing: false, expected: true, file: "01-daily-watch.md"
    }]
  }]
}
```
Missing report: `{missing: true, expected: true/false, title: "Did not arrive" / "Not due today"}`.

**Real content samples (use these for mock copy):**
- Daily Watch sections: URGENT/High Impact → Market & Stock Summary → RBI headlines-only → Financial Results → Rating Actions → Deals & M&A → Digital & Fintech → NPA & Asset Quality → Personnel → Friday Sector Deep Dive → Source Links (40+ links).
- Regulation sections: Regulatory Developments with [ADVISORY]/[CLARIFICATION]/[ENFORCEMENT] items, each with What + key points + MFL impact + source; penalty tables (NBFC | Date | Amount | Issue); Pipeline tracker (Revolving Credit draft Aug 6 → final ~Nov; Interest Rate Directions → eff. Apr 2027 HIGH IMPACT; Recovery Agent Conduct → eff. Jan 2027; SNFA norms → eff. Oct 1 2026).
- Podcast script: `days/YYYY-MM-DD/podcast-script.txt` — ~400-word morning read ("Good morning Achu! ...").

**Current CSS tokens:** --ink #1d1d1f, --mute rgba(0,0,0,.46), --blue #0071e3, glass cards rgba(255,255,255,.46/.88), radius 18–28px, blur 22–32px, serif Newsreader, sans system-ui/SF Pro. Evening: ink #f5f5f7, bg #050505, blue #2997ff.

**Demo explorations (not live):** `demo/` has 3 throwaway sketches — 001-cupboard-archive, 002-sunday-broadsheet, 003-evening-folio. Stitch redesign replaces these; feel free to borrow the "private newspaper" idea from 002.
