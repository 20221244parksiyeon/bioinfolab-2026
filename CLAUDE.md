# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A student's coursework repository for a Korean bioinformatics lab course (생물정보학실험). Each week's exercises live in their own `labNN/` folder. There is no build system, package manifest, linter, or test suite — work consists of small standalone Bash and Python 3 scripts run directly against FASTA files. Documentation, comments, and commit messages are written in Korean; match that.

## Layout conventions

- New weekly folders are created by copying the template: `cp -r lab-template labNN`. Each lab has:
  - `data/` — input/generated data (FASTA etc.)
  - `doc/` — reports, cheat sheets, result summaries (`.md`, `.tsv`)
  - `src/` — the student's scripts (`.sh`, `.py`)
- Labs are self-contained snapshots; the same script name (e.g. `batchinfo`, `gc`, `filter`) often reappears across labs in progressively different forms (lab05 Bash → lab06 Python → lab07 Python with a shared module). Edit the copy in the lab being worked on, not earlier ones.
- `resources/` holds instructor-provided sample data and scripts; top-level `src/` holds a few loose scripts.

## Running scripts

Scripts take file paths via `sys.argv` / positional args and are run from the lab folder, e.g.:

```
cd lab07
python3 src/countseq2.py data/seqs.fasta
python3 src/summary.py data/seqs.fasta doc/summary.tsv
# lab05-style Bash scripts
cd ../lab05
bash src/gc.sh data/seqs.fasta
```

From lab07 onward, scripts in `src/` import shared helpers via `from fasta import ...` (`lab07/src/fasta.py`: `read_fasta`, `gc_content`, `write_fasta`, `reverse_complement`, `length_stats`). Because of the plain import, run them with the script in `src/` (as above) so Python puts `src/` on the path. `read_fasta` keys sequences by the first word of the header and uppercases sequences. API docs: `lab07/src/README.md`, `lab09/doc/lab07.md`.

## Environment

Runs in GitHub Codespaces with one of four devcontainers under `.devcontainer/` (basic Python; conda/micromamba; sequence tools seqkit/blast/mafft/iqtree/fastqc/fastp; genome tools adding shovill/prokka). The README's week→environment table decides which one applies. `bash .devcontainer/check.sh` reports which tools are available. Don't install tools yourself except in the conda week — the course asks students to report missing tools to the instructor.

`.gitignore` excludes sequencing data (`*.fastq*`, `*.fq*`, `*.sra`), assembly/annotation output dirs (`shovill_*`, `spades_*`, `prokka_*`, `flye_out/`), and FastQC reports — re-download data with commands rather than committing it.

## Workflow

At the end of each lab the README's routine is `git add . && git commit -m "labNN 완료" && git push` (only commit/push when the user asks).
