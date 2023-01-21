from pathlib import Path
from typing import Final
from dataclasses import dataclass

from themes.theme import Theme
from themes.themes import onedark

THEME: Final[Theme] = onedark
THEME_FILE: Final[Path] = Path.cwd() / "themes/qtile_theme.txt"


@dataclass
class QtileTheme:
    background: list[str]
    contrast: list[list[str]]  # higher index -> lighter color
    foreground: list[str]
    accent: list[str]
    alert: list[str]


def convert_to_qtile(theme: Theme) -> QtileTheme:
    contrast = []
    for c in theme.contrast:
        contrast.append([c, c])

    return QtileTheme(
        background=[theme.background] * 2,
        contrast=contrast,
        foreground=[theme.foreground] * 2,
        accent=[theme.accent] * 2,
        alert=[theme.alert] * 2,
    )


def export(theme: Theme, filepath: Path):
    qtile_theme: QtileTheme = convert_to_qtile(theme)

    with open(filepath, "w") as file:
        file.write(str(qtile_theme))


if __name__ == "__main__":
    export(THEME, THEME_FILE)
