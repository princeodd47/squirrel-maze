[![CI](https://github.com/princeodd47/squirrel-maze/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/princeodd47/squirrel-maze/actions/workflows/ci.yml)
[![Code style: black](https://img.shields/io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# squirrel-maze
Goal: Using a pregenerated character, user can play through combat versus a pregenerated opponent.

## Prerequisites
squirrel_maze is built using poetry.

Installing poetry
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
```

## Run linters
```
make check
```

## Run unit tests
```
make tests
```

## Specifics
UI:
* User can start combat
* User can return from combat menu to main menu
* User can exit game from main menu

Combat:
* User can select from a list of options during combat
* These options are pulled per actor from a database
* Opponent automatically selects a single option during their turn
* Combat will end when either all friendlies or unfriendlies hp has reached 0.

Mechanics:
* Initiative generated based on dex, then level.

Backend:
* PC and NPC specifics are stored in TinyDB.
* All methods should pull data from database.

