from dataclasses import dataclass


@dataclass
class Primary:
    background: str
    contrast: list[str]  # Dark to bright
    foreground: str


@dataclass
class Normal:
    black: str
    red: str
    green: str
    yellow: str
    blue: str
    magenta: str
    cyan: str
    white: str


@dataclass
class Bright:
    black: str
    red: str
    green: str
    yellow: str
    blue: str
    magenta: str
    cyan: str
    white: str


@dataclass
class ColorScheme:
    primary: Primary
    normal: Normal
    bright: Bright
    accent: str
    wallpaper: str
