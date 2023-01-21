from pathlib import Path

from .theme import Theme


gruvbox = Theme(
    name="gruvbox",
    background="#282828",
    contrast=[
        "#3c3836",
        "#504945",
        "#665c54",
        "#7c6f64",
    ],
    foreground="#ebdbb2",
    wallpaper=Path.home()
    / "Themes/Gruvbox-GTK-Theme/wallpapers/gruvbox20.png",
    accent="#d65d0e",  # Orange
    alert="#cc241d"
    # black="#282828"
    # red="#cc241d"
    # green="#98971a"
    # yellow='#d79921'
    # orange="#d65d0e"
    # blue="#458588"
    # magenta="#b16286"
    # cyan="#689d6a"
    # white="#a89984"
)

dracula = Theme(
    name="dracula",
    background="#282a36",
    contrast=[
        "#343746",
        "#424450",
        "#535560",
        "#63646e",
    ],
    foreground="#f8f8f2",
    wallpaper=Path.home()
    / "Themes/Dracula-wallpapers/first-collection/dracula-wallpaper.svg",
    accent="#bd93f9",  # Blue
    alert="#ff5555"
    # black="#21222c",
    # red="#ff5555",
    # green="#50fa7b",
    # yellow="#f1fa8c",
    # blue="#bd93f9",
    # magenta="#ff79c6",
    # cyan="#8be9fd",
    # white="#f8f8f2",
)

catppuccin = Theme(
    name="catppuccin",
    background="#1E1E2E",
    contrast=[
        "#343547",
        "#3F4154",
        "#4A4C60",
        "#767A91",
    ],
    wallpaper=Path.home()
    / "Themes/Catppuccin-wallpapers/mandelbrot/mandelbrot_full_flamingo.png",
    foreground="#CDD6F4",
    accent="#F5C2E7",  # pink
    alert="#F38BA8",
    # black: "#45475A" # surface1
    # red: "#F38BA8" # red
    # green: "#A6E3A1" # green
    # yellow: "#F9E2AF" # yellow
    # blue: "#89B4FA" # blue
    # magenta: "#F5C2E7" # pink
    # cyan: "#94E2D5" # teal
    # white: "#BAC2DE" # subtext1
)

tokyonight = Theme(
    name="tokyonight",
    background="#24283b",
    contrast=[
        "#2E3347",
        "#383D53",
        "#4B516A",
        "#727998",
    ],
    wallpaper=Path.home()
    / "Themes/Tokyo-Night-GTK-Theme/wallpapers/tokyo-night31.png",
    foreground="#c0caf5",
    accent="#f7768e",  # red
    alert="#f7768e",
    # black:   '0x1d202f'
    # red:     '0xf7768e'
    # green:   '0x9ece6a'
    # yellow:  '0xe0af68'
    # blue:    '0x7aa2f7'
    # magenta: '0xbb9af7'
    # cyan:    '0x7dcfff'
    # white:   '0xa9b1d6'
)

everforest = Theme(
    name="everforest",
    background="#2d353b",
    contrast=[
        "#383F42",
        "#424849",
        "#575A57",
        "#807E73",
    ],
    wallpaper=Path.home()
    / "Themes/Everforest-GTK-Theme/wallpapers/everforest01.jpg",
    foreground="#d3c6aa",
    accent="#a7c080",
    alert="#e67e80",
    # black:   '#475258'
    # red:     '#e67e80'
    # green:   '#a7c080'
    # yellow:  '#dbbc7f'
    # blue:    '#7fbbb3'
    # magenta: '#d699b6'
    # cyan:    '#83c092'
    # white:   '#d3c6aa'
)

kanagawa = Theme(
    name="kanagawa",
    background="#1f1f28",
    contrast=[
        "#2B2B32",
        "#37363B",
        "#4F4D4D",
        "#7E7B71",
    ],
    wallpaper=Path.cwd() / "Pictures/wallpapers/the-great-wave-minimal.png",
    foreground="#dcd7ba",
    accent="#7e9cd8",
    alert="#c34043",
    # black:   '0x090618'
    # red:     '0xc34043'
    # green:   '0x76946a'
    # yellow:  '0xc0a36e'
    # blue:    '0x7e9cd8'
    # magenta: '0x957fb8'
    # cyan:    '0x6a9589'
    # white:   '0xc8c093'
)

onedark = Theme(
    name="onedark",
    background="#1e2127",
    contrast=[
        "#272B31",
        "#30343A",
        "#42464D",
        "#656A73",
    ],
    wallpaper=Path.cwd() / "Themes/OneDarkWallpapers/34.png",
    foreground="#abb2bf",
    accent="#e06c75",
    alert="#e06c75",
    # black:   '0x1e2127'
    # red:     '0xe06c75'
    # green:   '0x98c379'
    # yellow:  '0xd19a66'
    # blue:    '0x61afef'
    # magenta: '0xc678dd'
    # cyan:    '0x56b6c2'
    # white:   '0x828791'
)
