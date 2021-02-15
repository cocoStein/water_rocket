To put in ~/.gitconfigtrick for nice history:

    [user]
        name = Jérôme Dufour
        email = jerome.dufour@eduvaud.ch

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

