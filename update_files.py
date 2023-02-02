import re
from pathlib import Path
from subprocess import Popen


def update_str(
    content: str,
    replacements: list[tuple[str, str]],
) -> str:
    for target, replacement in replacements:
        pattern: re.Pattern[str] = re.compile(target)
        content = pattern.sub(replacement, content)

    return content


def apply_changes(
    file: Path,
    replacements: list[tuple[str, str]],
    command: list[str | Path] | None = None,
    template: Path | None = None,
):
    file.write_text(
        update_str(
            content=file.read_text()
            if template is None
            else template.read_text(),
            replacements=replacements,
        )
    )

    if command is not None:
        Popen(command)
