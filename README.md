# Tetris Clone

## Project Overview
This is a simple Tetris clone implemented in Python using the Pygame library.The goal is to complete lines by filling them with tetrominoes. Completed lines are cleared, and the player earns points.
The game ends if the tetromino stack reaches the top of the screen.


## How to Play
+ Use the arrow keys to move the falling tetromino left, right, or down.
+ Press the up arrow key to rotate the tetromino.
+ Press the space key to pause or resume the game.
+ Press 'Q' to quit the game.

## Controls
+ Left Arrow: Move tetromino left
+ Right Arrow: Move tetromino right
+ Down Arrow: Move tetromino down
+ Up Arrow: Rotate tetromino
+ Space: Pause/Resume
+ Q: Quit

## Scoring
+ Points are earned by completing lines.
+ The game displays the current score and the high score.
+ The game saves the high score in a file called high_score.txt.

## Requirements
+ Python 3.x
+ Pygame library

## Installation
+ Install Python: https://www.python.org/
+ Install Pygame: pip install pygame

## How to Run Tests
+ Navigate to the directory containing the tests.
+ Run the command: python test_pygame_tetris.py

## Test Cases
+ test_go_down: Tests the functionality of moving the tetromino down.
+ test_go_left: Tests the functionality of moving the tetromino to the left.
+ test_go_right: Tests the functionality of moving the tetromino to the right.
+ test_turn_i: Tests the rotation functionality for the I-shaped tetromino.
+ test_turn_j: Tests the rotation functionality for the J-shaped tetromino.
+ test_display_game_over: Tests the display of the game over screen.

## Instructions
+ Each test case evaluates specific functionalities of the Tetris clone.
+ The setUp method initializes necessary components for testing.
+ The tearDown method cleans up resources after each test.
+ Run the tests using the unittest module.
