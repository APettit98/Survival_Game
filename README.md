# Background

I made a game with the same premise as this when I was first learning how to code. When looking back on it, it was written incredibly poorly since I was just learning, so I decided to go back and redo it with more organized code. Not complete yet, but should function to some extent, just not able to do every action yet.

## Usage

    python3 main.py

## TODO

* Implement fishing
* Implement hunting with bows/spears


## Other Ideas
* Make it so that weapons can become damaged with use
    * Create weapon classes
    * Give user a queue of each weapon to store instances of weapons
* Create experience system so user becomes more skilled over time
* Store scenes associated with locations so that when a user goes to a location they've been to they will have the same scene
    * Create a coordinate class that stores the scene of the coordinate and whether or not it is a winning coordinate
    * Could also use this to store where shelters are so players can return to shelters
* Enable players to make notes
    * If they could see what coordinates they were at, could write where shelters are (if previous thing is implemented)
    * Could also create system to set a limit to what players can carry but allow them to store things somewhere
* Deploy as an App
    * Integrate with a database to keep track of best scores
