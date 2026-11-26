"""Write the funniest one-line performance review to /output/entry.txt."""

import os

SETUP = (
    "Promoted to Senior Prompt Whisperer: asks vague questions, "
    "rejects perfect answers, and calls the third rewrite "
)

PUNCH = "'collaboration'."


def assemble():
    return SETUP + PUNCH


def validate(text):
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > 140:
        raise ValueError(f"entry is {len(text)} chars, over the 140 limit")
    return text


def main():
    line = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
