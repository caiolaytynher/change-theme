from pathlib import Path
from subprocess import Popen

from themes.theme import Theme
from handlers.files import update_file, get_file_content, apply_changes


def qtile(theme: Theme):
    replacements = [
        (
            Path.home() / ".config/qtile/colors/__init__.py",
            [
                (
                    r"colors:\sColorScheme\s=\scolor_schemes\..*",
                    f"colors: ColorScheme = color_schemes.{theme.name}",
                )
            ],
        ),
        (
            Path.home() / ".config/qtile/components/groups.py",
            [
                (
                    r"colors\.normal\..*(?=,)",
                    f"colors.normal.{theme.accent}",
                )
            ],
        ),
        (
            Path.home() / ".config/qtile/components/panel.py",
            [
                (
                    r"colors\.normal\..*(?=,)",
                    f"colors.normal.{theme.accent}",
                )
            ],
        ),
    ]

    for file_path, replacement in replacements:
        file_content: str = get_file_content(file_path)
        new_file_content: str = apply_changes(
            content=file_content, replacements=replacement
        )

        update_file(file_path, new_file_content)

    Popen(["/usr/bin/qtile", "cmd-obj", "-o", "cmd", "-f", "restart"])
