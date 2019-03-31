[![CircleCI](https://circleci.com/gh/princeodd47/squirrel-maze.svg?style=svg)](https://circleci.com/gh/princeodd47/squirrel-maze)

# squirrel-maze
Goal: Using a pregenerated character, user can play through combat versus a pregenerated opponent.

UI Specifics:
* User can start combat
* User can return from combat menu to main menu
* User can exit game from main menu

Combat Specifics:
* User can select from a list of options during combat
* These options are pulled per actor from a database
* Opponent automatically selects a single option during their turn
* Combat will end when either all friendlies or unfriendlies hp has reached 0.

Mechanics Specifics:
* Initiative generated based on dex, then level.

Backend Specifics:
* PC and NPC specifics are stored in TinyDB.
* All methods should pull data from database.
