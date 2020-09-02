# Python-Soduku-Solver
Python script that takes soduku question of user's choice and solve it.
It used the technique of recursion and backtracting.

## Prerequisite
Python3 is required.

## Instruction
1. Run `python3 solver.py`.
2. Enter your soduku row by row, with a space between numbers:
```
Please input the sudoku:
0 3 0 0 0 0 0 8 0
5 0 0 0 6 0 0 0 0
0 0 0 0 0 8 2 1 9
0 0 7 9 0 0 0 6 0
0 0 0 0 0 7 0 0 2
0 0 0 2 0 0 1 0 0
0 7 1 3 4 0 0 0 0
2 0 0 0 0 0 4 0 3
0 0 9 0 0 0 0 0 0
```
3. Follow the instruction, press enter to start solving
```
- - - - - - - - - - - - - 
| 0 3 0 | 0 0 0 | 0 8 0 | 
| 5 0 0 | 0 6 0 | 0 0 0 | 
| 0 0 0 | 0 0 8 | 2 1 9 | 
- - - - - - - - - - - - - 
| 0 0 7 | 9 0 0 | 0 6 0 | 
| 0 0 0 | 0 0 7 | 0 0 2 | 
| 0 0 0 | 2 0 0 | 1 0 0 | 
- - - - - - - - - - - - - 
| 0 7 1 | 3 4 0 | 0 0 0 | 
| 2 0 0 | 0 0 0 | 4 0 3 | 
| 0 0 9 | 0 0 0 | 0 0 0 | 
- - - - - - - - - - - - - 
Press <Enter> to start solving.
```
4. Answer and elapsed time are output at the end:
```
Ans:
- - - - - - - - - - - - - 
| 1 3 2 | 4 7 9 | 6 8 5 | 
| 5 9 8 | 1 6 2 | 7 3 4 | 
| 7 6 4 | 5 3 8 | 2 1 9 | 
- - - - - - - - - - - - - 
| 4 2 7 | 9 1 3 | 5 6 8 | 
| 9 1 5 | 6 8 7 | 3 4 2 | 
| 6 8 3 | 2 5 4 | 1 9 7 | 
- - - - - - - - - - - - - 
| 8 7 1 | 3 4 5 | 9 2 6 | 
| 2 5 6 | 8 9 1 | 4 7 3 | 
| 3 4 9 | 7 2 6 | 8 5 1 | 
- - - - - - - - - - - - - 
Elapsed time:  0:00:02.597124
```
