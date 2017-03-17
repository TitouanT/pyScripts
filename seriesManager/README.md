# Serie Manager

I watch many series and I want to keep track of the last episode I have seen for all of them.
So I write this little manager to do that for me.


# How to use it ?

If you just clone the repo then all the data is about what I am currently watching.

+ To see all the data:

	`./main.py`

+ To delete a serie:

	`./main.py del <index>` (the index is the number at the begining of each line)

+ To add a serie:

	`./main.py new <"title in quote if it contains spaces"> <season> <episode>` (season = 0 if you don't know yet)

+ To add an episode:

	`./main.py up <index> [Ss]` (put an 's' at the end if it have to pass a season)

+ To set the value:

	`./main.py set <index> <season> <episode>`

+ To display the known, unknown or current series:

	`./main.py <known|unknown|current>`

+ To toogle the current status:

	`./main.py toggle <index>`

# is there some shortcuts ??

glad you ask, each option have a short name:

| name    | short |
| :---:   | :---: |
| new     | n     |
| up      | +     |
| set     | s     |
| known   | k     |
| unknown | uk    |
| current | c     |
| toggle  | t     |
| del     | d     |
