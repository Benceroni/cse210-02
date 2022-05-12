# cse210-02 Hi-Lo Game

Are you willing to test your wits and luck? Play Hi-Lo, you won't be disappointed. The rules are simple. Depending in
the first card drawn you can guess if the next one will be higher or lower. If you are correct you will be awarded 100 points.
If you are not 75 points will be taken. You start with 300 points and finish when you reach 0 points or you surrender.

## Getting Started
---
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and 
browse to the project's root folder. Start the program by running the following command.
```
python3 hi-lo or py hi-lo
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the dice folder and click the "run" button.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- hi-lo               (source code for game)
  +-- game              (specific classes)
    +-- deck.py         (deck class)
    +-- director.py     (director class)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0

## Authors
---
* Spencer Bell (bel21032@byui.edu)
* Dallas Eaton (deaton879@byui.edu)
* Julian Hernandez (hernandezjuliang44@gmail.com)
* Mike Lewis (wyoming.c64@gmail.com)
* Jaden McCarrey (jadenmccarrey@gmail.com)


---
## Overview

Hi-Lo (sometimes "Hilo", or other variations) is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. Points are won or lost based on whether or not the player guessed correctly.

---
## Rules

Hi-Lo is played according to the following rules.

- The player starts the game with 300 points.
- Individual cards are represented as a number from 1 to 13.
- The current card is displayed.
- The player guesses if the next one will be higher or lower.
- The the next card is displayed.
- The player earns 100 points if they guessed correctly.
- The player loses 75 points if they guessed incorrectly.
- If a player reaches 0 points the game is over.
- If a player has more than 0 points they decide if they want to keep playing.
- If a player decides not to play again the game is over.

---
## Requirements

The program must also meet the following requirements.

- [x] The program must include a README file.
- [x] The program must include class and method comments.
- [x] The program must have at least two classes.
- [x] The program must remain true to game play described in the overview.

---
## Have Some Fun

Have some fun by enhancing the game any way you like. A few ideas are as follows.

- [x] Enhanced input validation.
- [x] Enhanced game play and game over messages.
- [ ] Enhanced game display, e.g. card suits



