**Everything in the assets/ directory belongs to Five Nights at Frickbaers 3 by 
SpookyRick, credits to him and check out his game, it's kinda awesome**

## Installation guide

On the right of this page there should be a releases tab, you can download a .zip
file with all the files necessary to run the program. Download it and extract it
somewhere, and now you can run the .exe and Rodney should show up at the bottom
right if you did everything correctly!

Do note that both the assets/ directory and config.py MUST be in the same folder
as the .exe, otherwise the app will not work. Since they're separated from the
.exe, you can actually customize them. For more information on how to, check out
`config.py` and `assets/README.md`

Unfortunately, only Windows users can use github releases to run this program at
the moment. If you're using another OS, you might want to clone this repo and
build the binary yourself using PyInstaller. The command I ran to package this app
is `pyinstaller --name RodneySP --onefile --icon=assets/icon.ico --windowed run.py`.
Everything before it should be easy enough to run with the help of a Youtube
tutorial on how to clone a python github project or something