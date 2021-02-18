# Terminal

This file will gives some information on basic commands available in the
terminal. Keep in mind, that using a terminal might seem a waste of time in the
beginning, but it is actually extremely powerful.

## Shell

When a terminal is open, it loads a `shell` which provide an environment to
interpret the commands typed. Some shells are more user friendly than other.
The default shell on linux is called `bash` and recently OSX decided to use
`zsh`. I (Jérôme) personally have been using `zsh` for years now and I would
advise using it as it comes with some very handy tools and is easy to configure
thanks to [ohmyzsh][1].

## Basic command

To get more explanation on unix commands, please consult this [tutorial][2].

### `cd`: change directory

+ `cd ~/path/to/your/directory` allows you to move to any directory
+ `cd` brings you back to your home directory which contain all your personal
  files
+ `cd ..` brings you a label before. If you were in `/home/toto/this/folder/`,
  the previous command brings you to `/home/toto/this/`
+ `cd -` brings you to the previous location. If you were in
  `/home/toto/this/folder/` and then moved to `/home/tutu/that/other/folder`,
  typing this commend would send you back to `/home/toto/this/folder`

### `cp`: copy

### `mv`: move

### `rm`: remove


[1]:https://github.com/ohmyzsh/ohmyzsh
[2]:https://maker.pro/linux/tutorial/basic-linux-commands-for-beginners
