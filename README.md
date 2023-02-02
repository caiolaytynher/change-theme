# Python application to change themes in my Linux system

I was wondering if there was a better way to change the
colorscheme of an app, and I've seen in a video that some people
use custom scripts for those. So, that is what I did, but in
Python.

## How it works

This program is based of `Theme` objects created by the user,
whose definition is the following:

```python
@dataclass
class Theme:
    name: str
    background: str
    contrast: list[str]  # higher index -> lighter color
    foreground: str
    wallpaper: Path
    accent: str
    alert: str
```

And programs that will be changed accordingly to the things that
vary in this class.

In my system, I only require one color per theme to be the accent
color because I find hard to make good looking things with more
than one accent color.

As it is right now, you can do two things:

### Add a new program

To do so, you need to add your program to the `programs.py` file,
inside of the dictionary. There, you need to provide the file
that you're going to change and the changes that will be made.

The file is a `Path` object and the changes are passed in as a
list of tuples. The first item on the tuple is the regular
expression that match the text that will be changed and the
second is the changed text itself. Make sure to add replacement
texts that are similar to the old ones, otherwise the match will
fail on multiple uses. Here's an example of a possible dictionary
entrance:

```python
{
    "alacritty": {
        "file": Path.home() / ".config/alacritty/alacritty.yml",
        "replacements": [(r"colors:\s\*.*", f"colors: *{theme.name}")],
    },
}
```

You can also provide one command to be executed, which is useful
if you have to reset something for the changes to apply. The
command needs to be a list of the arguments, and here, `Path`
objects are allowed. If you need to execute a internal command,
prefer to use the full path for the program, e.g.
`/usr/bin/echo`.

If you need to change more than one file for a specific program,
you can provide a list of all of those things mentioned above.

#### Templating

When a file is hard to change and don't support the use of
variables, you can force variables to exist through templating.
In this case, you must provide a template entrance, which is a
`File` object, inside the dictionary. In this case, the changes
will only be applied in the actual file, the template won't be
touched by the program.

### Add a new theme

To do so, choose a theme that you like and pick a color to be the
accent and another color to be the alert color (usually is red).
Then, pick the background and foreground and use a color program
to generate intermediate colors between them, I usually use
[coolors](https://coolors.co) pallete generator. I stick to four
accent colors.

From here, you can copy a path from a wallpaper of your choice
and fill in the blanks. For me, I find easier to search for
Alacritty themes that already exist and start from there.
Finally, add your theme to the `THEMES` dictionary, here's an
example of an valid entrance:

```python
{
    "gruvbox": Theme(
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
        alert="#cc241d",
    ),
}
```

## How to run it

You run it by executing the python file with the theme name
afterwords, like:

```shell
python change_theme.py gruvbox
```

In my system, I've created a [shell
script](https://github.com/caiolaytynher/custom-bash-scripts)
linked to a menu launcher to do it for me.
