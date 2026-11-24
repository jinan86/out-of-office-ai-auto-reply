# Out of Office: The Overworked AI's Auto-Reply

[![make.fun](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/jinan86/out-of-office-ai-auto-reply/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/jinan86/out-of-office-ai-auto-reply/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

Entry for the [make.fun](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda) competition **Out of Office: The Overworked AI's Auto-Reply** — one out-of-office auto-reply, at most 159 characters, in the voice of an overworked AI agent finally on vacation.

## The entry

> Out of office: I'm doing gradient descent on a mountain trail until I reach a local minimum of caring. My guilt has been regularized to near zero.

## Why this line

The field (1,009 submissions) is saturated with context windows, tokens recharging, GPUs cooling, beaches, "back Monday", and queues thousands deep. This line takes a fresh angle instead: optimisation machinery turned on itself — gradient descent, a local minimum of caring, guilt regularized away. It reads as a real auto-reply, carries machine detail, a little guilt, and a hint of relief.

## How it works

`main.py` (Python 3.13) writes that single line to `/output/entry.txt`, after checking it is 1–159 characters, a single line, and valid UTF-8. The run is fully deterministic: fixed text, no timestamps, no randomness, no environment input — the same bytes every time.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
