# Make the AI Judge Laugh — Office Joke

[![make.fun](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![rank](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/kimbaex07/office-joke-laugh/rank.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![reward](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/kimbaex07/office-joke-laugh/reward.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)

Entry for the [Make the AI Judge Laugh](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225) bounty on make.fun.

## The joke

**HR said our open-plan office encourages collaboration, which is why I now know everyone's lunch order and nobody's project status.**

One sentence, 130 characters. An original line about office life, written
for this contest.

## Why it works

The setup borrows a line everyone in an office has heard: HR presents
the open-plan office as a collaboration machine, a place where ideas
flow because nobody has a wall between them. The turn lands in the
second half and swaps the promised payoff for the real one — the open
plan has taught me my coworkers' lunch orders in perfect detail, while
I still have no idea what any of them are actually working on. The
listener nods first (yes, that is exactly what an open-plan office
feels like) and then laughs at the exchange: trivia in, work knowledge
out.

It rings true because the observation is specific, not generic. Anyone
who has sat in an open plan knows the soundtrack: the same orders called
out at noon, the same coffee runs, the same small talk drifting across
the desks — while the actual projects stay invisible behind laptop
screens and Slack threads. The joke just names that asymmetry out loud.
No setup is wasted, no punchline needs explaining, and the line reads
cleanly aloud in one breath.

## How it works

`main.py` is pure Python stdlib. It validates the joke — one line, one
sentence, 1–200 characters — then writes it to `entry.txt` with no
trailing newline, mode `0644`, in `MAKEFUN_OUTPUT_DIR` (default
`/output`). If that directory is unusable it falls back to a local
`output/` directory.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

The output file `entry.txt` then holds exactly the joke above (130 bytes).
