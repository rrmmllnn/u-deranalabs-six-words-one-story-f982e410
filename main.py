"""Six Words, One Story — a make.fun entry.

This program composes one six-word story and saves it to
/output/entry.txt, where the grader reads it.

The story:
    Planted the garden. She never came.

A man prepares the ground for a shared future — seeds, soil,
patience — for someone who never arrives. The garden grows
anyway, which is both the hope and the heartbreak: the life
he imagined keeps blooming without her.
"""

from pathlib import Path

STORY_TEXT = "Planted the garden. She never came."
DESTINATION = Path("/output/entry.txt")


def write_story() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(STORY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    write_story()
