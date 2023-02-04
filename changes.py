import re
from pathlib import Path
from subprocess import Popen
from dataclasses import dataclass


def update_str(
    content: str,
    replacements: list[tuple[str, str]],
) -> str:
    """
    Modify a string based of a regular expression and a replacement. The
    function will match the regex with the string contents and apply the
    substitution in each place it appears.
    """
    for target, replacement in replacements:
        pattern: re.Pattern[str] = re.compile(target)
        content = pattern.sub(replacement, content)

    return content


@dataclass
class ChangesToApply:
    """Parameters for the apply_changes function."""

    file: Path
    replacements: list[tuple[str, str]]
    command: list[str | Path] | None = None
    template: Path | None = None


def apply_changes(changes: ChangesToApply):
    """
    Update the file contents with the specified changes, which include a
    regex substitution and command execution.
    """
    changes.file.write_text(
        update_str(
            content=changes.file.read_text()
            if changes.template is None
            else changes.template.read_text(),
            replacements=changes.replacements,
        )
    )

    if changes.command is not None:
        Popen(changes.command)
