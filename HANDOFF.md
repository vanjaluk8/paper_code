# HANDOFF — Continue work on another machine

> Written by Claude on **2026-08-21** after a repo cleanup + history rewrite.
> Read this first when you pick this up on a new PC. It explains **what changed,
> what is still pending, and how to finish the two manual steps.**
>
> **UPDATE (2026-08-21):** the repo has since been **split into two** fresh repos —
> `slr_engine` (pipeline code; see sibling checkout) and this one, `papers_code`
> (manuscripts, `papers_repo/`, PRISMA package). The manual steps below (force-push /
> key rotation) now apply per-repo and the old combined history was **not** force-pushed.

---

## TL;DR — what still needs doing (do these first)

- [ ] **1. Force-push the rewritten history** to GitHub (hashes changed → must be `--force`).
- [ ] **2. Rotate the Anthropic API key** that was previously committed (get a new one, put it in `.env`).

Both are manual, machine-dependent steps. Everything else about the repo is *done* and ready to share with reviewers.

---

## 1. Push the rewritten history to GitHub

The repository was **history-rewritten** (PDFs and a leaked API key scrubbed from all
commits). Commit hashes are **different** from whatever was on GitHub before, so a
normal push will be rejected. From your machine (where your GitHub SSH key works):

```bash
# on branch main
git push --force --set-upstream origin main
```

Remotes are already configured (`origin` → `git@github.com:vanjaluk8/litreview-peft-p2p-adapters.git`).

> **One-time caution:** this overwrites the remote history. Old commits (and the old
> leaking API key) will still be cached on GitHub server-side / in any forks. If you
> want a fully clean public history, **re-create the repo** (or a fresh `git clone` of
> this local one) and push to a brand-new empty repo instead of force-pushing.

## 2. Rotate the Anthropic API key

The key `sk-ant-api03…` was hardcoded in `slr_engine/snowballing/app/config.py` and
was committed before the cleanup. Although it's now scrubbed from both the working
tree *and* all history locally, it may already be on GitHub, so **treat it as leaked:**

1. Revoke/recreate it in the Anthropic console.
2. Put the new key in your local `.env` (gitignored); do **not** hardcode it:

   ```bash
   # slr_engine/snowballing/.env  (or app/.env)
   ANTHROPIC_API_KEY=sk-ant-…
   ```

The code now requires the key via environment/`.env` — it deliberately has **no**
hardcoded fallback, and LLM paths (`app/screen.py`, `app/abstract_review.py`) print a
clear error if it's missing. This is intentional.

---

## What the cleanup changed (recap)

- **`.git` shrank from ~248 MB → ~12 MB.** Nothing is lost on disk — `git rm --cached`
  only untracked files; your local PDFs/CSVs are still where they were.
- **Reference PDFs are no longer in git.** They live locally (and in Zotero).
  The old `.gitignore` rule was buggy (`writing_materials/pdfs/` vs the real
  `validation/pdfs/`); it's fixed to `**/pdfs/` + `**/*.pdf`.
- **Intermediate `snowball_output/*.csv` are no longer tracked.** Only the audited
  deliverables are kept: `13_final_reading_list_*.csv`, `PRISMA_summary*.md`.
- **Two pipeline generations were disentangled:**
  - *Canonical (keep):* `run_pipeline.sh` + `main.py` + `app/` package → numbered `00…13_*.csv`.
  - *Archived:* `slr_engine/archive/snowball-aided-manual-export/` holds the manual
    Scopus/WoS export post-processors + superseded `make_visuals.py`.
- `download_pdfs.py` was fixed to use the newest `13_final_reading_list_*.csv`
  (was pointing at stale `S8_final_reading_list.csv`).

## Three most recent commits

```
9518e49 docs: add canonical-pipeline repo map; remove hardcoded API key; fix S8 ref
cce8a67 Tidy pipeline generations: archive manual-export scripts, fix stale S8 ref
1c36b7f Stop tracking generated artifacts: PDFs and snowball intermediates
```

## The canonical pipeline (for reviewers)

The one command that runs the whole SLR pipeline:

```bash
cd slr_engine/snowballing
bash run_pipeline.sh              # Semantic Scholar only (default)
bash run_pipeline.sh --engine all # all four engines
```

Entry points: `main.py` (CLI orchestrator), `app/` (screen, merge, enrich, prisma,
visualise, engines). Full detail is in `slr_engine/snowballing/README.md` under
"Repository layout — what is *the* pipeline?".

---

## Files that exist only locally (now gitignored — do NOT commit)

These are on this machine's working tree but not tracked, by design:

- `writing/slr_methodology_paper/validation/pdfs/**` — reference PDF library
- `slr_engine/snowballing/snowball_output/**` — regenerated intermediates/logs/notebooks
  (except the kept deliverables above)
- `papers_repo/*.pdf` — methodology reference PDFs
- any `.env`, `.venv`, `.idea/`, `__pycache__/`

If you `git status` on the new machine and see a sea of ignored files, that's expected.

---

## Backup

A full pre-rewrite backup bundle (with the original history) was left at:

```
/tmp/repo-backup-20260821-154648.bundle
```

Only needed if something about the rewrite surprises you. The machine-local files
were never deleted, so this is belt-and-suspenders.
