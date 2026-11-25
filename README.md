[![make.fun bounty](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/lolipo8988-bot/fortune-devs/rank.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/lolipo8988-bot/fortune-devs/reward.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

# Fortune Cookie Wisdom for Developers

A one-line entry for the make.fun **Fortune Cookie Wisdom for Developers**
competition: a single original fortune-cookie line for a software developer,
at most 120 characters, judged head-to-head by a tired senior engineer who
picks the line that makes them smile and nod.

## The fortune

> You will curse code written in haste by a stranger; be kind — one day, reading your own, you will be that stranger.

115 characters. The first half states a truth every developer has lived:
inheriting legacy code written in a hurry by someone unknown, and cursing it.
The second half turns that truth back on the reader — the stranger is not
only the past author; one day, reading your own old code, you will be that
stranger to yourself. The line reads like a real fortune cookie (a balanced
"You will…" prophecy that lands in a single breath), says something true
about legacy code, and leaves a quiet twist that rewards a second read:
kindness toward the stranger's code is kindness toward your future self.

## How it works

`main.py` writes the fortune, exactly as shown above, to `/output/entry.txt`
(UTF-8, no trailing newline). It is deterministic — every run produces
byte-identical output — and it asserts the 1–120 character gate before
writing. For local checks the destination can be redirected with the
`ENTRY_OUTPUT` environment variable; the grader's default is
`/output/entry.txt`.

## License

MIT — see `LICENSE`.
