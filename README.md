[![CircleCI](https://circleci.com/gh/princeodd47/squirrel-maze.svg?style=svg)](https://circleci.com/gh/princeodd47/squirrel-maze)

# squirrel-maze
Goal: Using a pregenerated character, user can play through combat versus a pregenerated opponent.

## Prerequisites
squirrel_maze is built using poetry.

Installing poetry
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
```

Install test dependencies
```
poetry run python3 -m pip install types-tabulate
poetry run mypy --install-types
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

