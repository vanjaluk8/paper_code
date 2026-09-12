# Major #20 — Top-Up Search Query Set (draft only, not executed)

Per the review: a four-month gap exists between the search date
(2026-04-14 to 2026-05-12) and the anticipated submission month
(September 2026), in a field with 38 corpus records from 2024 alone.

This file drafts the query set for a top-up search covering that gap.
**No queries have been run and no results have been judged** — per the
task instructions, running live database searches and screening the
results is the author's judgement call, not something to execute here.

## Approach

Reuse the exact 20 Boolean queries already in Appendix C
(`sections/12_appendix.tex`, §C.1–C.2), verbatim, changing only the
publication-date filter to cover the gap. This keeps the top-up search
methodologically identical to the original — same terms, same venue
restrictions — so any new hits are attributable to the passage of time,
not a change in search strategy.

**Scopus**: append `AND PUBYEAR > 2026` (or, if the interface allows a
precise cutoff, `AND PUBYEAR = 2026 AND (PUBMONTH >= 5)`) to each of the
existing Q1–Q10 Scopus strings, replacing that query's original
`PUBYEAR > YYYY` clause with an explicit lower bound tied to the last
search date (2026-05-12) rather than each query's original broad
lower bound.

**Web of Science**: the WoS queries in Appendix C (§C.2) do not carry an
explicit `PY=` filter in every query the way the Scopus set does; add
`PY=2026` (or the platform's date-range picker set to 2026-05-13 through
the search-execution date) to each of the 10 WoS queries.

## Execution checklist (for the author)

- [ ] Run all 10 Scopus queries with the amended date filter; export results.
- [ ] Run all 10 WoS queries with the amended date filter; export results.
- [ ] De-duplicate against the existing 123-record final corpus (by DOI,
      then normalised title — same method as
      `verify/boolean_recall.py`, which can be reused directly by
      pointing it at the new export files).
- [ ] Screen any genuinely new candidates against the same eligibility
      criteria used throughout (§3.2 / Appendix A.3).
- [ ] Report: how many new candidates were found, how many passed
      screening, and whether any of the review's eight open gaps
      (§9.4) have already been addressed by work published in the gap
      window — this last judgement is scientific interpretation and is
      the author's to make, not something to infer from a hit count.

## What this file deliberately does NOT do

- Does not run any query.
- Does not estimate or guess how many new records a top-up search would
  return.
- Does not claim any existing gap has or hasn't been closed by newer
  work — the review's own question ("Have any of the eight gaps been
  closed since April?") is preserved verbatim as an open question in
  `OPEN_QUESTIONS.md`, not answered here.
