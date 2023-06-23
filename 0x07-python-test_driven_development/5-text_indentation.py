#!/usr/bin/python3
"""Defines a function that prints a text with indentation."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If `text` is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()

    punctuation_marks = [".", "?", ":"]
    lines = []

    current_line = ""
    for char in text:
        current_line += char
        if char in punctuation_marks:
            lines.append(current_line.strip())
            current_line = ""

    if current_line:
        lines.append(current_line.strip())

    indented_text = "\n\n".join(lines)
    print(indented_text)
