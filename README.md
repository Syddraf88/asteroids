# asteroids
boot.dev asteroids guided project.

This Project follows the course material for base game project and I have elected to enhance the base game with a few additional features. which are detailed here in the read me.

1. Score and Persistent Leader board.
   You score 1 point for each time the split method is ran on an asteroid. and using the json module there is a persistent leader board stored in the champions.json file the game creates when it runs.

   In the event of a high scoring round, the game will promp the player to input their initals, and then store that information along with their score as a tupple in the high scores list. it will then sort them in decending order and slice the list to only keep the top five results. that will then be displayed as part of the game over summary. as well as dump the list back to the champions.json file it created to make the list persistent.

   This does mean that the user running the game needs to have write permission to the directy the game is being run off of.

2. Acceleration and Drag
   I have also made tweaks to the movement system to mimic acceleration instead of a flat movement rate as well as drag to slow a players ship gradually when there is no active input.

   these settings still need some tweaking but are working as intended at this time.
