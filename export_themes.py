from pathlib import Path
from typing import Final
from dataclasses import dataclass

import themes

THEME_FILE: Final[Path] = Path.cwd() / "qtile_theme.txt"


@dataclass
class QtileTheme:
    background: list[str]
    contrast: list[list[str]]  # higher index -> lighter color
    foreground: list[str]
    accent: list[str]
    alert: list[str]


def convert_to_qtile(theme: themes.Theme) -> QtileTheme:
    contrast: list[list[str]] = []
    for c in theme.contrast:
        contrast.append([c, c])

    return QtileTheme(
        background=[theme.background] * 2,
        contrast=contrast,
        foreground=[theme.foreground] * 2,
        accent=[theme.accent] * 2,
        alert=[theme.alert] * 2,
    )


def export(theme: themes.Theme, file: Path):
    qtile_theme: QtileTheme = convert_to_qtile(theme)
    file.write_text(str(qtile_theme))


if __name__ == "__main__":
    export(
        themes.THEMES["onedark"],
        THEME_FILE,
    )
