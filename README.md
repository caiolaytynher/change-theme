# Python application to change themes in my Linux system

I was wondering if there was a better way to change the
colorscheme of an app, and I've seen in a video that some people
use custom scripts for those. So, that is what I did, but in
Python.

## How it works

As it is right now, you can do two things:

### Add a new app

To do so, you need to create a config function inside a config
file, then import the function to the main file and add it to the
configs list. Reducing the amount of steps for add a new app is
in the plans.

### Add a new theme

Add a new theme, on the other hand, is way easier, and it is what
you'll do the most. You only need to create a new instance of the
`Theme` class. You need to add it to the `VALID_THEMES` constant,
though.

## How to run it

You run it by executing the python file with the theme name
afterwords, like:

```{shell}
python main.py gruvbox
```

In my system, I've created a [shell
script](https://github.com/caiolaytynher/custom-bash-scripts)
linked to a menu launcher to do it for me.
