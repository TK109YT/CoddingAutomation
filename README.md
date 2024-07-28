# CoddingAutomation

A simple script in python to create the distribution of diferent types of codding projects in seconds.

---

## Instalation

1. Clone the repo or copy the script.

Use this to clone the whole repo

`git clone https://github.com/Zyroxsh/CoddingAutomation` 

Or use this to get the script

`wget https://raw.githubusercontent.com/Zyroxsh/CoddingAutomation/main/Codding.py`


2. This step is optional but you can move the script to any route of your path to execute it easy

First look your path with this

`echo $PATH`

Then choose one of those routes and put the script there

`mv Codding.py <PATH-ROUTE>`

Now give him the execution permision with

`chmod +x Codding.py`

At this moment you can execute it as a built-in command

---

## Usage

Until this moment the program can create a new project and open it, or if you have a project open it.
For the moment the templates for the projects are *general*, *web*, *python*, *blank* and *other*.
The script can open projects with **Visual Studio Code** (`code` in linux) or with **NeoVim** (`nvim` in linux).


### Create a new project

> [!IMPORTANT]
> You can see all the options using `Codding.py -h` 


`Codding.py -c -t <PROJECT-TYPE> -p <PATH> -e <EDITOR> -n <PROJECT-NAME>`

* Where *PROJECT-TYPE* the type of project.
* Where *PATH* the path were the project will be created.
* Where *EDITOR* the editor to use when the project will be opened.
* Where *PROJECT-NAME* the name of the new project.


### Open an existing project

`Codding.py -o -p <PROJECT-PATH> -e <EDITOR>`

* Where *PROJECT-PATH* the path where is the project to open.
* Where *EDITOR* the editor to use.


---

Copyright (c) 2024 zyrox.sh. All Rights Reserved.
