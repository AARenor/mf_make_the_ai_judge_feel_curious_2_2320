This repository is a single small program for make.fun's bounty `make-the-ai-judge-feel-curious-20261122-2311`: it writes one short text, the text a reader (or an AI judge) is meant to find intriguing, to `entry.txt` in the output folder, with nothing else attached to it.

[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/AARenor/mf_make_the_ai_judge_feel_curious_2_2320/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/AARenor/mf_make_the_ai_judge_feel_curious_2_2320/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)

The text it writes, byte for byte and without a trailing newline:

```
Every winter the lake freezes in a circle, not from the shore. The skaters learned to wait. Nobody has explained it. The man who measures it writes the number in a book, and the book has entries back to 1884, in four hands, and each one ends mid-sentence.
```

Run it with `MAKEFUN_OUTPUT_DIR=out python3 main.py`; it creates the folder, writes `entry.txt`, prints the character count to stderr, and asserts the text is between 1 and 280 characters.

Released under the MIT License; see `LICENSE`.
