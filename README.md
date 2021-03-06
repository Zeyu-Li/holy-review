# A Holy Review

## Intro

HolyC is a programming language that can be found in [TempleOS](https://templeos.org/) and is best described as C derivative with inline assembly support.

The best way to experience this is to download [TempleOS](https://templeos.org/) and run it on a virtual machine (like VirtualBox)

## Install and Use

The best tutorial I can find for downloading and running TempleOS is this [YouTube Video: youtube.com/watch?v=NK0lPrrdAxw](https://www.youtube.com/watch?v=NK0lPrrdAxw)

After installing to the drive and rebooting, you will be prompted with a chance to go through the tutorials

### Keyboard Commands

Some common keyboard commands not included in [[2]](#shortcuts) are

* <kbd>Ctrl</kbd> + <kbd>M</kbd> for menu
* <kbd>Ctrl</kbd> + <kbd>Y</kbd> to delete a whole line
* <kbd>Shift</kbd> + <kbd>Del</kbd> to cut
* Alt+Backspace Undo
* <kbd>f1</kbd> for help
* <kbd>f5</kbd> to run the script while in the editor
* <kbd>Esc</kbd> to escape out of almost everything

To find a list of all the commands do Help [<kbd>f1</kbd>]->Key Map

### CLI Commands

\*Note all commands will be post-fixed by `;` since these are the direct calls to the functions themselves

* `Dir;` to ls (same as DOS)
* `Cd("FolderName");` to go to the folder called `FolderName` within the current level directory
* `Ed("FileName.HC");` to jump into the editor for a file called `FileName.HC`



## About HolyC

Strongly recommend going through the Help [<kbd>f1</kbd>]->HolyC manual to learn more

* A file name ending in `.Z` wile `Hello.HC.Z` will be compressed
* Main function is not needed
* Convenient conditions of `0<a<=10` and the like are included
* Switch statements are very optimized and are more expressive. Some things include ranges
* `no_warn` stmt will suppress unused var warning
* `$` is the escape char
* No `#define` or `typedef` although classes are a thing
* No `continue`, only `goto`
* Different `printf` codes (see manual)



Compiler for HolyC is JIT (just in time)

## Resources

[1] Install TempleOS on VirtualBox: [youtube.com/watch?v=NK0lPrrdAxw](https://www.youtube.com/watch?v=NK0lPrrdAxw)

<a name=shortcuts></a>

[2] Keyboard shortcuts: [github.com/Passw/TempleOS-DivineOS#keyboard-shortcuts](https://github.com/Passw/TempleOS-DivineOS#keyboard-shortcuts)

[3] About the late Terry Davis, the creator: [Down the Rabbit Hole](https://www.youtube.com/watch?v=UCgoxQCf5Jg)



## License

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) 

