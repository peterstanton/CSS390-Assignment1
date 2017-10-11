# CSS390-Assignment1

This assignment is an introduction to scripting in UWB's CSS 390: Special Topics course on Scripting.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This assignment requires access to a Linux environment with an installed Python 2.7 interpreter. More specifically this code was written and tested in 2.7.12

This code executes using print functionality from Python 3 in Python 2, using an import from __future__ library. Using a Python 3 interpreter this import can be removed.

### Installing

Download both script files. 

Place the files into the ROOT of the music directory to be scanned.

## Running the tests

Run the scripts by opening a bash terminal in the root directory where the scripts are located.

Invoke the base case script by typing: "./PeterStanton-Assignment1-base.sh"

Invoke the bonus script by typing: "python bonus.py"

### Break down into end to end tests

BASE:

This file is a bash script.

To find the total number of tracks, it performs a recursive search of the current directory, filtering all files through a search for the pattern .ogg to only select music files, otherwise it would include the scripts themselves in the count. The results are passed to wc to tally the results.

Total artists are tallied similarly, however grep instead passes the results to cut, which extract the field which contains the artists name. Those are then sorted and duplicates removed, leaving the list of artists, which is passed to wc for counting.

Multi-genre artists are more complicated. When the results reach cut, multiple fields are extracted, namely the genre and artist fields
in the format: "genre/artist", which are sorted into unique entries. The names of the artists themselves are extracted, and those which appear more than once (and thus had multiple genre entries) are printed.

Some albums have more than one disk. In those cases, the fourth field is occupied by disk and a number. By cutting out the album, disk field, and song of all songs, and searching for a regular expression pattern of the word disk together with a number, all multiple disk song entries can be identified. Then the results are piped to cut to remove the disk number and song names, leaving only album names. Duplicates are removed and the results are printed.


BONUS:

The first two results are simple. Python can invoke bash subprocesses, which is adequate to again find the total tracks and artists.

I did not manage to find multi-genre artists. I ran out of time.

For multidisk albums, lists are created for artists and albums. We then iterate through the directory and subdirectories using os.walk(). Files we find are split along the delimiter "/" in their path into another list for processing. If an artist's name, as found in the artist field, has not been found, it is added to our list of artists, and the album is added to the album list. If an artist has been seen before, the new album is appended to the corresponding album list entry with a new line character for simplicity of eventual printing.

When directory processing is complete, the artist and album lists are iterated through simnultaneously and printed. Since artists and their first album were placed into the list at the same time and multiple albums are registered through string concatenation with the first entry, the albums match up with the artist.

## Assumptions 

1.) Any test data used will follow the same subdirectory format, with all files in the leaf folders. 
2.) Test data will follow the same structure of genre/artist/album/possibly disk#/*.ogg
3.) All test data used will be .OGG files.
4.) Minor whitespace differences are acceptable.
5.) Script files are not intended to count towards the totals of files in the directories.
6.) We will never have an album with a name matching this regex pattern: [dD]isk\s*[1-9]
7.) User is running at least Python 2.7.
8.) User is running Bash 4.3 or later.
9.) User is running the scripts in an Ubuntu environment.
10.) There will be no files in the directory and subdirectories that contain the filename pattern ".ogg" other than the Ogg Vorbis music files the user intends to process.


## Built With

Ubuntu 16.04
Python 2.7.12
GNU bash, version 4.3.48(1)-release (x86_64-pc-linux-gnu)
JetBrains Pycharm 2017.2.3
VIM - Vi IMproved 7.4
gedit - Version 3.18.3



## Authors

* **Peter Stanton** -- Student


## Acknowledgments

* Assorted classmates who answered miscellaneous questions.
And in no particular order:

* https://stackoverflow.com/questions/493386/how-to-print-without-newline-or-space
* https://www.tutorialspoint.com/python/os_walk.htm
* https://stackoverflow.com/questions/3777301/how-to-call-a-shell-script-from-python-code
* https://docs.python.org/2/library/subprocess.html
* http://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python
* http://grokbase.com/t/python/python-list/088x3kmq77/iterating-two-arrays-at-once
* https://www.tutorialspoint.com/python/string_split.htm

* https://www.cyberciti.biz/faq/find-command-exclude-ignore-files/
* https://stackoverflow.com/questions/9402961/adding-newline-characters-to-unix-shell-variables
* https://www.computerhope.com/unix/ugrep.htm
* https://unix.stackexchange.com/questions/52534/how-to-print-only-the-duplicate-values-from-a-text-file
* http://www.folkstalk.com/2012/02/cut-command-in-unix-linux-examples.html
* https://stackoverflow.com/questions/3382936/sort-uniq-in-linux-shell

