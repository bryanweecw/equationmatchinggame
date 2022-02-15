## Installation

1. Install Python 3.10.10
2. Run `pip install pygame`
3. Ensure that the following .wav files are in the same directory as the MainGameFile.py:
   a. buzz.wav
   b. congratsplayable.wav
   c. congratsunplayable.wav
   d. ding.wav
   e. highscore.wav
   f. kahootbgm.wav
   g. shortbuzz.wav
   h. ticksound.wav
4. Run MainGameFile.py to start the game

## Libraries Used

1. Pygame
2. Random
3. Tkinter

## Instructions

1. A random equation will be generated by the game
2. Click the buttons to match the numbers/ operators in the equation shown
3. Be careful! The button positions change each time you click them
4. Pay attention to the 30 second timer - If the time runs out, or if you misclick, your score gets reset!

## Compatibility

The GUI has been tested and works on MacOS. If you are running a different OS, you might have issues with the size of the window. You can configure this by modifying the window.geometry() function called in line 450.

## Unit Testing

To run unit tests, ensure you have pytest installed, with `pip install pytest`, then run `pytest unittests.py`

## Github Repo Link

Project files can be found at this [link](https://github.com/bryanweecw/equationmatchinggame)
