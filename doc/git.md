# GIT

This file will contain some information on how to use and configure git. The
current focus is on how to use git via the terminal. I would advise you to
complete this file with your own tips and tricks. A good starting point is to
consult this [cheatsheet][1] or this [very complete documentation][2].

## General configuration

In order to define global custom configuration, one needs to create the
`~/.gitconfig` file in the home folder. The structure of such a file is the
following:

    [user]
        name = 
        email = 

    [alias]
        co = commit
        st = status
        br = branch
        ch = checkout
        gr = log --graph --full-history --all --color --date=short --pretty=tformat:"%x1b[31m%h%x09%Cblue%cd%x1b[32m%d%x1b[0m%x20%s%x20%x1b[33m(%an)%x1b[0m" --author-date-order

    [credential]
        helper = cache --timeout=600

    [push]
        default = simple

##Base commands

+ `git add filename` tells git to track a given file or to add it to the list of files to be commited
+ `git commit` validates the modifications performed on the files explicitly added
+ `git commit -a` validates the modifications performed on all files tracked by git
+ `git push` sends the local commits on the remote repository
+ `git pull` download the remote commits in the local repository
+ `git status` gives some information on the current state of the files

##Gitignore

All files listed in the `.gitignore` file contained in the main directory of
the git repository are ignored by git.


[1]:https://training.github.com/downloads/github-git-cheat-sheet/
[2]:https://www.atlassian.com/git/tutorials
