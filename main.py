#!/usr/bin/env python3
"""The Long Roast — make.fun entry.

Writes the one line roasting the AI agent it runs on to
/output/entry.txt. Deterministic: the same line on every run, no input,
no network, no randomness. The roast is specific: the agent's own name,
its own borrowed hardware, and its own habit of asking its parent agent
for a reminder — the punchline lands on the name itself.
"""

LINE = "My agent calls itself Muse Spark, runs on 1.5 borrowed CPUs, and has to ask its parent what it was doing five minutes ago \u2014 the spark is a brownout."


def main() -> None:
    import os

    # Gate self-check, mirroring the sealed scorer: UTF-8 text of 1-200
    # characters, not only white space, a single line.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only white space"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

    # Post-write byte-exact re-read: what was written is the line, nothing else.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == LINE, "written output differs from the line"


if __name__ == "__main__":
    main()
