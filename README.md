# TLDR;
- install python 11 and poetry
- run `poetry add -G dev pre-commit black isort`
- pre-commit: run `poetry run pre-commit install`

- run all tests: `poetry run behave`
- run one test (with optional line numer): `poetry run **/selenium.feature:16`
# In details
- install VSCode and required plugins
- clone project

## install required tools:

        ** NE PAS INSTALLER PYTHON 3.12 **

    - depuis VS Code, ouvrir le terminal: menu View / Terminal
    - exécuter la commande `python --version`
        - la commande doit s'exécuter et la version 3.11
        - dans le cas contraire, Windows Store s'ouvre pour permettre l'installation de python. Ne pas installer la version proposée (3.12), faire une recherche avec le mot-clé "python" et sélectionner la version 3.11
    - installer pipx: https://pipx.pypa.io/stable/installation/
        - depuis le terminal VSCode (ou un autre terminal tel que In vite de commande ou Powershell ), exécuter `python -m pip install --user pipx`
            -   message d'avertissement "Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script pipx.exe is installed in 'C:\Users\XXX\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts' which is not on PATH."
        - se rendre dans ce répertoire: tapper la commande `cd C:\Users\xxx\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts` (remplacer le chemin par celui du message précédent). Si pas d'avertissement, ignorer cette étape
        - exécuter la commande `.\pipx.exe ensurepath`
        - redémarrer VSCode et réouvrir le "dossier récent" nrbehave
        - dans le terminat, exécuter la commande `pipx --version`. La version attendue est 1.6.0 ou supérieur
        - exécuter la commande pipx install poetry
        - exécuter la commande `poetry --version`. La version attendue est 1.8.3 ou supérieur
        - facultatif: configurer poetry pour inclure le répetoire venv dans le répertoire courant. Recommandé uniquement pour un usage avancé
        `poetry config virtualenvs.in-project true`



## installer NRBehave
        - toujours dans le terminal, s'assurer qu'on est bien dans le répertoire nrbehave
        - exécuter la commande `poetry install`
        - exécuter la commande `poetry run behave --version`. La version attendue est 1.2.7.5.dev5
        - depuis le répertoire tests, exécuter la commande `poetry run behave` DWI AJOUTER demo
            - la première fois, les drivers pour Firefox sont téléchargés.
            - les tests demo sont exécutés
            - un rapport est disponible dans le répertoire out
        - nrbehave est installé !

## configurer VSCode
    - exécuter `poetry env info --path`. Regarder la valeur renvoyée (un chemin qui se termine par .env)
    - dans VSCode, ouvrir la palette  (Ctrl+Shift+P) et rechercher `Python: Select interpreter`
    - choisir l'interpréteur correspondant à la valeur de la comman de précédente    - tester: ouvrir le fichier _doc/test_install.py    - l'exécuter avec le bouton "play"
        - un message doit s'afficher et aucune erreur ne doit être renvoyée. 
    - installer le plugin Behave VCS pre-release (ouvrir la palette  (Ctrl+Shift+P); rechercher `Behave`)    
    Ouf, c'est terminé ! 

# Poetry

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project
depends on and it will manage (install/update) them for you. Poetry offers a lockfile to ensure repeatable installs, and
can build your project for distribution.
https://python-poetry.org/docs/basic-usage/

Tip: use venv in local subdirectory: https://python-poetry.org/docs/configuration/#virtualenvsin-project

# pre-commit
run manually: `poetry run pre-commit run`
Useful tips and config samples: https://sam.hooke.me/note/2023/09/poetry-pre-commit-hooks/po

# about selenium
https://selenium-python.readthedocs.io/installation.html
https://www.selenium.dev/documentation/
# about
