# week_7

Title: Greed 

Purpose: 
To gather as much gems as possible, its an endless game until player wants to quit. 

Description:
-The player is identify as (#) which can move from left to right, using the Actor it position along the bottom of the screen
-Gem file creates the gems(*) which appear randomly in the screen, as well the rocks (0)
    -As the player moves around the screen, when it touches the gems(*), they earn points and they loose points when they touch the rocks. 
-The gems and rocks are automatically remove once they are been touch, another gem or rock will appear randomly afterwards. 
-The game will continue until the player decides to quit. 


Project Structure:
__main.py__ - calls game.start_game() from game.py file which will start the game, imports all the information in the game file which will allow the game to start. 

game.py - initialize by importing gem file, player, rock, screen, and color. These will create the screen with the gems and rocks appear, it will have the player # at the bottom of the screen. 




Required Software: Terminal, Any IDE 

Team member name            | Email address
Nelson Muchonji Bifwoli       bif20001@byui.edu 
Guillermo Quinteros           qui22003@byui.edu
Erika Ramirez                 ramirezerika328@gmail.com
Daniel                        das22001@byui.edu