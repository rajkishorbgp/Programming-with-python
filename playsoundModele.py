'''
he playsound module contains only one thing - the function (also named) playsound.
It requires one argument - the path to the file with the sound you’d like to play. This may be a local file, or a URL.
There’s an optional second argument, block, which is set to True by default. Setting it to False makes the function run asynchronously.
On Windows, uses windll.winmm. WAVE and MP3 have been tested and are known to work. Other file formats may work as well.
On OS X, uses AppKit.NSSound. WAVE and MP3 have been tested and are known to work. In general, anything QuickTime can play, playsound should be able to play, for OS X.
On Linux, uses GStreamer. Known to work on Ubuntu 14.04 and ElementaryOS Loki. I expect any Linux distro with a standard gnome desktop experience should work.
If you’d like other Linux distros (or any other OS) to work, submit a PR adding in support for it, but please make sure it passes the tests (see below).

'''

from playsound import playsound
playsound('D:\\mus.mp3')
