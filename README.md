# TLDR;
- install python 11 and poetry
- run `poetry add -G dev pre-commit black isort`
- pre-commit: run `poetry run pre-commit install`
# Poetry

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project
depends on and it will manage (install/update) them for you. Poetry offers a lockfile to ensure repeatable installs, and
can build your project for distribution.
https://python-poetry.org/docs/basic-usage/

Tip: use venv in local subdirectory: https://python-poetry.org/docs/configuration/#virtualenvsin-project

# pre-commit
run manually: `poetry run pre-commit run`
Useful tips and config samples: https://sam.hooke.me/note/2023/09/poetry-pre-commit-hooks/po
