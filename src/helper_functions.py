from typing import Pattern


def change_line(
    filepath: str,
    target_regex: Pattern[str],
    replacement_text: str,
) -> None:
    with open(filepath, "r") as file:
        file_string = "".join(file.readlines())

    matches = target_regex.finditer(file_string)
    for match in matches:
        start, end = match.span()
        file_string = file_string.replace(file_string[start:end], replacement_text)

    with open(filepath, "w") as file:
        file.write(file_string)
