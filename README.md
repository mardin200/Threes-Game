# Threes-Game
Threes is tiny puzzle that grows on you. We have implemented a simple, console-based mode of this game in Python.
The codes are written based on Python 3 and do not require any dependencies to run.

A sample input is given in the code but It is possible to receive inputs from the console.
The inputs include the following in order:
N: An integer that represents the dimensions of the game table.
start_state: A nested matrix that defines the initial state of the game.
Movements: is a string that determines the order of movements in the game, where R represents the Right, L for Lefrt, U for Up and D for Down.
Next, the number of moves determined(equals to len(Movements)), the tuple is received (k,d), where d represents the new number (1 or 2 or 3) that is added to the table and (k%m) is the index of the cell in which the new number should be placed from left to right or from top to bottom.

After execution, the final state of the puzzle will be shown and the points obtained will be shown at the end.
