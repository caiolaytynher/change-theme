import re
from typing import Pattern


def change_line(
    filepath: str,
    target: str,
    replacement: str,
) -> None:
    pattern: Pattern[str] = re.compile(target)

    with open(filepath, "r") as file:
        file_string = "".join(file.readlines())

    modified_file_string = pattern.sub(replacement, file_string)

    with open(filepath, "w") as file:
        file.write(modified_file_string)


def change_lines(
    filepath: str,
    targets: list[str],
    replacements: list[str],
) -> None:
    if len(targets) != len(replacements):
        raise Exception("The targets and the replacements should have the same size.")

    patterns: list[Pattern[str]] = [re.compile(target) for target in targets]

    with open(filepath, "r") as file:
        file_string = "".join(file.readlines())

    modified_file_string = file_string
    for (
        pattern,
        replacement,
    ) in zip(patterns, replacements):
        modified_file_string = pattern.sub(replacement, modified_file_string)

    with open(filepath, "w") as file:
        file.write(modified_file_string)


def change_template(
    input_filepath: str,
    targets: list[str],
    replacements: list[str],
    output_filepath: str,
) -> None:
    if len(targets) != len(replacements):
        raise Exception("The targets and the replacements should have the same size.")

    patterns: list[Pattern[str]] = [re.compile(target) for target in targets]

    with open(input_filepath, "r") as file:
        file_string = "".join(file.readlines())

    modified_file_string = file_string
    for pattern, replacement in zip(patterns, replacements):
        modified_file_string = pattern.sub(replacement, modified_file_string)

    with open(output_filepath, "w") as file:
        file.write(modified_file_string)
