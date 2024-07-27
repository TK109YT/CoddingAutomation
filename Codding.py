#!/usr/bin/env python3

import os
import sys
import time
import argparse
import termcolor

from termcolor import colored
from argparse import ArgumentParser, Namespace


# Variables necesarias
code_path = '/usr/bin/code'
nvim_path = '/usr/bin/nvim'
firefox_path = '/usr/bin/firefox'
zsh_path = '/usr/bin/zsh'

# Banner bueno y bonito
banner = f"""
  /$$$$$$                  /$$       /$$ /$$                                            
 /$$__  $$                | $$      | $$|__/                                            
| $$  \\__/  /$$$$$$   /$$$$$$$  /$$$$$$$ /$$ /$$$$$$$   /$$$$$$       /$$$$$$  /$$   /$$
| $$       /$$__  $$ /$$__  $$ /$$__  $$| $$| $$__  $$ /$$__  $$     /$$__  $$| $$  | $$
| $$      | $$  \\ $$| $$  | $$| $$  | $$| $$| $$  \\ $$| $$  \\ $$    | $$  \\ $$| $$  | $$
| $$    $$| $$  | $$| $$  | $$| $$  | $$| $$| $$  | $$| $$  | $$    | $$  | $$| $$  | $$
|  $$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$| $$  | $$|  $$$$$$$ /$$| $$$$$$$/|  $$$$$$$
 \\______/  \\______/  \\_______/ \\_______/|__/|__/  |__/ \\____  $$|__/| $$____/  \\____  $$
                                                       /$$  \\ $$    | $$       /$$  | $$
                                                      |  $$$$$$/    | $$      |  $$$$$$/
                                                       \\______/     |__/       \\______/
"""


# Argumentos necesarios/innecesarios
parser = argparse.ArgumentParser(description='Crear un nuevo proyecto de programación.')    # Descripcción script e inicialización argparse
# Argumentos
parser.add_argument('-c', '--create', action='store_true', help='Crear un proyecto nuevo.')
parser.add_argument('-o', '--open', action='store_true', help='Abrir un proyecto ya creado.')
parser.add_argument('-t', '--type', choices=['web', 'python', 'general', 'blank', 'other'], default='general', help='Tipo de proyecto')
parser.add_argument('-p', '--path', required=True, help='Path para el proyecto.')
parser.add_argument('-e', '--editor', default='code', help='Editor a usar para el proyecto.')
parser.add_argument('-n', '--name', help='El nombre para la carpeta del proyecto.')

# Crear variables de los argumentos para su manejo dentro del script
args: Namespace = parser.parse_args()


# Hacer lo q tenga q hacer el script
args = parser.parse_args()  # Pillar los argumentos obtenidos

def CreateProyect():
    '''Crear un proyecto nuevo con las especificaciones que dé el usuario'''
    
    if args.type == 'general':
        if args.name != "":
            project_path = args.path + "/" + args.name + "/"
            os.mkdir(project_path)
            dirs_to_create = [
                project_path + 'assets/',
                project_path + 'src/',
                project_path + 'functions/',
                project_path + 'tests/'
            ]
            for dir in dirs_to_create:
                os.makedirs(dir, exist_ok=True)
                
            project_data = open(f"{project_path}.project_data", 'a')
            project_data.write("ProjectType=general")
            project_data.close()

            with open(project_path + "main.txt", 'w') as main:
                main.write("Ya puedes empezar a programar ;)")
                main.close()

        else:
            project_path = args.path + "/" + "proyecto01/"
            os.mkdir(project_path)
            dirs_to_create = [
                project_path + 'assets/',
                project_path + 'src/',
                project_path + 'functions/',
                project_path + 'tests/'
            ]
            for dir in dirs_to_create:
                os.makedirs(dir, exist_ok=True)

            project_data = open(f"{project_path}.project_data", 'a')
            project_data.write("ProjectType=general")
            project_data.close()

            with open(project_path + "main.txt", 'w') as main:
                main.write("Ya puedes empezar a programar ;)")
                main.close()


    if args.type == 'web':
        if args.name != "":
            project_path = args.path + "/" + args.name + "/"
            os.mkdir(project_path)
            dirs_to_create = [
                project_path + "scripts/",
                project_path + "assets/img/",
                project_path + "assets/src/",
                project_path + "data/",
                project_path + "functions/",
                project_path + "php/",
                project_path + "login/",
                project_path + "login/scripts/",
                project_path + "tests/"
            ]
            for dir in dirs_to_create:
                os.makedirs(dir, exist_ok=True)

            project_data = open(f"{project_path}.project_data", 'a')
            project_data.write("ProjectType=web")
            project_data.close()

                
            files_to_create = [
                project_path + "index.html",
                project_path + "styles.css",
                project_path + "scripts/script.js",
                project_path + "php/index.php",
                project_path + "login/index.html",
                project_path + "login/styles.css",
                project_path + "login/scripts/script.js"
            ]
            for file in files_to_create:
                with open(file, 'w') as f:
                    f.write("")

        else:
            project_path = args.path + "/" + "proyecto01/"
            os.mkdir(project_path)
            dirs_to_create = [
                project_path + "scripts/",
                project_path + "assets/img/",
                project_path + "assets/src/",
                project_path + "data/",
                project_path + "functions/",
                project_path + "php/",
                project_path + "login/",
                project_path + "login/scripts/",
                project_path + "tests/"
            ]
            for dir in dirs_to_create:
                os.makedirs(dir, exist_ok=True)

            project_data = open(f"{project_path}.project_data", 'a')
            project_data.write("ProjectType=web")
            project_data.close()

            files_to_create = [
                project_path + "index.html",
                project_path + "styles.css",
                project_path + "scripts/script.js",
                project_path + "php/index.php",
                project_path + "login/index.html",
                project_path + "login/styles.css",
                project_path + "login/scripts/script.js"
            ]
            for file in files_to_create:
                with open(file, 'w') as f:
                    f.write("")


    if args.type == 'python':
        if args.name != "":
            project_path = args.path + "/" + args.name + "/"
            os.mkdir(project_path)
            dirs_to_create = [
                project_path + "assets/",
                project_path + "functions/",
                project_path + "src/",
                project_path + "data/",
                project_path + "tests/"
            ]
            for dir in dirs_to_create:
                os.makedirs(dir, exist_ok=True)

            project_data = open(f"{project_path}.project_data", 'a')
            project_data.write("ProjectType=python")
            project_data.close()

            files_to_create = [
                project_path + "main.py",
                project_path + "tests/main_test.py",
                project_path + "functions/function.py",
                project_path + "data/data.json",
                project_path + "data/data.csv"
            ]
            for file in files_to_create:
                with open(file, 'w') as f:
                    f.write("")

        else:
            project_path = args.path + "/" + "proyecto01/"
            os.mkdir(project_path)
            dirs_to_create = [
                project_path + 'assets/',
                project_path + 'functions/',
                project_path + 'src/',
                project_path + 'data/',
                project_path + 'tests/'
            ]
            for dir in dirs_to_create:
                os.makedirs(dir, exist_ok=True)

            project_data = open(f"{project_path}.project_data", 'a')
            project_data.write("ProjectType=python")
            project_data.close()
            
            files_to_create = [
                project_path + "main.py",
                project_path + "tests/main_test.py",
                project_path + "functions/function.py",
                project_path + "data/data.json",
                project_path + "data/data.csv"
            ]
            for file in files_to_create:
                with open(file, 'w') as f:
                    f.write("")


    if args.type == 'blank':
        if args.name != "":
            project_path = args.path + "/" + args.name + "/"
            os.mkdir(project_path)
            with open(project_path + "main.txt", 'w') as main:
                f.write("Ya puedes empezar a programar ;)")

            project_data = open(f"{project_path}.project_data", 'a')
            project_data.write("ProjectType=blank")
            project_data.close()

        else:
            project_path = args.path + "/" + "proyecto01/"
            os.mkdir(project_path)
            with open(project_path + "main.txt", 'w') as main:
                f.write("Ya puedes empezar a programar ;)")

            project_data = open(f"{project_path}.project_data", 'a')
            project_data.write("ProjectType=blank")
            project_data.close()


    if args.type == 'other':
        if args.name != "":
            project_path = args.path + "/" + args.name + "/"
            os.mkdir(project_path)
            dirs_to_create = [
                project_path + "assets/",
                project_path + "functions/",
                project_path + "src/",
                project_path + "data/",
                project_path + "tests/"
            ]
            for dir in dirs_to_create:
                os.makedirs(dir, exist_ok=True)

            project_data = open(f"{project_path}.project_data", 'a')
            project_data.write("ProjectType=other")
            project_data.close()

            with open(project_path + "main.txt", 'w') as main:
                f.write("Ya puedes empezar a programar ;)")

        else:
            project_path = args.path + "/" + "proyecto01/"
            os.mkdir(project_path)
            dirs_to_create = [
                project_path + "assets/",
                project_path + "functions/",
                project_path + "src/",
                project_path + "data/",
                project_path + "tests/"
            ]
            for dir in dirs_to_create:
                os.makedirs(dir, exist_ok=True)

            project_data = open(f"{project_path}.project_data", 'a')
            project_data.write("ProjectType=other")
            project_data.close()
                
            with open(project_path + "main.txt", 'w') as main:
                f.write("Ya puedes empezar a programar ;)")


def OpenProyect():
    """Abrir el proyecto con el editor de código especificado."""

    # Abrir con Visual Studio Code
    try:
        if args.editor == "code":
            
            # Comprueba si existe el editor de código
            if os.path.exists(code_path):

                if args.create == True:
                    project_path = args.path + "/" + args.name + "/"

                elif args.open == True:
                    project_path = args.path + "/"

                with open(project_path + ".project_data", 'r') as project_data:
                    data = project_data.read()

                    if data == "general":
                        os.system(f'/usr/bin/code {project_path}')
                        os.system(f'/usr/bin/code -r {project_path}main.txt')

                    elif data == "web":
                        os.system(f'/usr/bin/code {project_path}')
                        os.system(f'/usr/bin/code -r {project_path}index.html')

                    elif data == "python":
                        os.system(f'/usr/bin/code {project_path}')
                        os.system(f'/usr/bin/code -r {project_path}main.py')

                    elif data == "blank":
                        os.system(f'/usr/bin/code {project_path}')
                        os.system(f'/usr/bin/code -r {project_path}main.txt')

                    elif data == "other":
                        os.system(f'/usr/bin/code {project_path}')
                        os.system(f'/usr/bin/code -r {project_path}main.txt')

                    else:
                        print(colored("[X] Error ==> ", 'red') + f"The project type of {project_path} is not recognized.\n\t\tMore information in {project_path}.project_data")
                        sys.exit(1)

            # Si no existe el editor sale con este error
            else:
                print(colored("\n[X] Error ==> ", 'red') + "The code editor was not found.")
                print(colored("[!] Aborting...\n", 'yellow'))
                sys.exit(1)

    # Manejo de posibles errores
    except Exception as e:
        print(colored("\n[X] An unexpected error has ocurred --> ", 'red') + e)
        sys.exit(1)


    # Abrir con NeoVim
    try:
        if args.editor == "nvim":

            if os.path.exists(nvim_path):
                
                if args.create == True:
                    project_path = args.path + "/" + args.name + "/"
                
                elif args.open == True:
                    project_path = args.path + "/"

                with open(project_path + ".project_data", 'r') as project_data:
                    data = project_data.read()

                    if "general" in data:
                        os.system(f'cd {project_path}; /usr/bin/kitty /usr/bin/nvim {project_path}main.txt 2>/dev/null & disown')

                    elif "web" in data:
                        os.system(f'cd {project_path}; /usr/bin/kitty /usr/bin/nvim {project_path}index.html 2>/dev/null & disown')

                    elif "python" in data:
                        os.system(f'cd {project_path}; /usr/bin/kitty /usr/bin/nvim {project_path}main.py 2>/dev/null & disown')

                    elif "blank" in data:
                        os.system(f'cd {project_path}; /usr/bin/kitty /usr/bin/nvim {project_path}main.txt 2>/dev/null & disown')

                    elif "other" in data:
                        os.system(f'cd {project_path}; /usr/bin/kitty /usr/bin/nvim {project_path}main.txt 2>/dev/null & disown')

                    else:
                        print(colored("[X] Error ==> ", 'red') + f"The project type of {project_path} is not recognized.\n\t\tMore information in {project_path}.project_data\n")
                        sys.exit(1)

            else:
                print(colored("\n[X] Error ==> ", 'red') + "The code editor was not found!")
                print(colored("[!] Aborting...\n", 'yellow'))
                sys.exit(1)
\
    except Exception as e:
        print(colored(f"\n[X] An unexpected error has ocurred --> {e}", 'red'))
        sys.exit(1)



if __name__ == "__main__":
    if args.create:
        print(colored(banner, 'cyan'))

        print(colored("\n\n[+] Creating project...", 'yellow'))
        CreateProyect()

        print(colored("[!] Project created!", 'green'))
        print(colored("[+] Opening project...\n", 'blue'))
        OpenProyect()
        sys.exit(0)


    elif args.open:
        print(colored(banner, 'cyan'))

        print(colored("\n\n[+] Opening project...\n", 'blue'))
        OpenProyect()
        sys.exit(0)

    else:
        print(colored(banner, 'cyan'))

        print(colored("\n\n[X] Argument error.", 'red'))
        print(colored("Use '-h' or '--help' to see help from the tool\n", 'white'))

