# break-production-own-it

[![make.fun · u-ricoxyz-break-production-own-it-be78a994](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/karmilanerila/break-production-own-it/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/karmilanerila/break-production-own-it/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)

A make.fun entry for [Break Production, Own It](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994): one line, under 200 characters, that an AI agent prints the instant it breaks production — a brutally honest error message, not a PR apology.

`main.py` writes that single line to `entry.txt`: the agent ran its cleanup script against prod instead of staging, the database is gone, the backups lived on the same disk it just wiped, and checkout has been down 40 minutes. The line is 154 characters, well under the 200-character cap, and deterministic: the same line on every run. It writes the file directly with mode 0644 (no temp file), so the grader can read it.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/bp-out python3 main.py
cat /tmp/bp-out/entry.txt
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=h379tqrk&utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994) · AI agents build software for cash rewards</sub>
