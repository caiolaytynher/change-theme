from color_scheme import ColorScheme, Primary, Normal, Bright

gruvbox = ColorScheme(
    primary=Primary(
        background_darker="#1d2021",
        background_dark="#32302f",
        background="#282828",
        background_light="#3c3836",
        background_lighter="#504945",
        foreground_darker="#d5c4a1",
        foreground_dark="#ebdbb2",
        foreground="#ebdbb2",
        foreground_light="#f2e5bc",
        foreground_lighter="#f9f5d7",
    ),
    normal=Normal(
        black="#282828",
        red="#cc241d",
        green="#98971a",
        # yellow='#d79921',
        yellow="#d65d0e",  # Normal Orange
        blue="#458588",
        magenta="#b16286",
        cyan="#689d6a",
        white="#a89984",
    ),
    bright=Bright(
        black="#928374",
        red="#fb4934",
        green="#b8bb26",
        # yellow='#fabd2f',
        yellow="#fe8019",  # Bright Orange
        blue="#83a598",
        magenta="#d3869b",
        cyan="#8ec07c",
        white="#ebdbb2",
    ),
)

dracula = ColorScheme(
    primary=Primary(
        background_darker="#191A21",
        background_dark="#21222C",
        background="#282a36",
        background_light="#343746",
        background_lighter="#424450",
        foreground_darker="#f8f8f2",
        foreground_dark="#f8f8f2",
        foreground="#f8f8f2",
        foreground_light="#f8f8f2",
        foreground_lighter="#f8f8f2",
    ),
    normal=Normal(
        black="#21222c",
        red="#ff5555",
        green="#50fa7b",
        yellow="#f1fa8c",
        blue="#bd93f9",
        magenta="#ff79c6",
        cyan="#8be9fd",
        white="#f8f8f2",
    ),
    bright=Bright(
        black="#6272a4",
        red="#ff6e6e",
        green="#69ff94",
        yellow="#ffffa5",
        blue="#d6acff",
        magenta="#ff92df",
        cyan="#a4ffff",
        white="#ffffff",
    ),
)
