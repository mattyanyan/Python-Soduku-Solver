import datetime

su = [
    # For debug

    # [5, 0, 0, 4, 0, 0, 0, 3, 0],
    # [0, 0, 0, 0, 1, 0, 6, 0, 0],
    # [0, 0, 0, 0, 8, 0, 0, 4, 0],
    # [0, 0, 0, 0 ,0 ,0 ,0 ,0, 0],
    # [0, 0, 1, 3, 4, 0, 0, 0, 0],
    # [0, 7, 3, 2, 0, 0, 0, 0, 9],
    # [6, 8, 0, 0, 0, 0, 0, 0, 7],
    # [0, 0, 0, 5, 0, 0, 0, 2, 0],
    # [2, 1, 0, 0, 6, 0, 0, 0, 0]

    # [0, 8, 5, 7, 0, 0, 0, 0, 0],
    # [0, 0, 2, 0, 0, 5, 0, 0, 4],
    # [0, 0, 0, 0, 0, 8, 0, 0, 0], 
    # [0, 0, 0, 0, 0, 0, 5, 8, 2],
    # [0, 0, 0, 0, 7, 9, 4, 0, 0],
    # [0, 0, 0, 0, 6, 0, 7, 0, 0],
    # [4, 0, 0, 0, 0, 0, 0, 2, 0],
    # [0, 7, 0, 0, 0, 0, 0, 0, 1],
    # [9, 0, 0, 1, 3, 0, 0, 0, 0]
]

# Get sudoku input
def input_su():
    print("Please input the sudoku:")

    for i in range(9):
        new_row = [int(i) for i in input().split(" ")]
        while len(new_row) != 9:
            print("Error. Please input again.")
            new_row = [int(i) for i in input().split(" ")]
        su.append(new_row)
    
    print("\n*********************************************\n")

# Print sudoku
def print_su(su):
    for i in range(len(su)):
        if i % 3 == 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(su[0])):
            if j % 3 == 0:
                print("| ", end="")

            print(su[i][j], end=" ")
            
            if j == len(su[0]) - 1:
                if j == 8:
                    print("| ")
                else:
                    print("| ", end="")
        
        if i == len(su) - 1:
            print("- - - - - - - - - - - - - ")

# Return a empty cell's position           
def isEmpty(su):
    for i in range(len(su)):
        for j in range(len(su[0])):
            if su[i][j] == 0:
                return (i, j)
    
    return None

# Check if the entered num is valid or not by
# Compare it row by row, col by col, with its 3x3 box 
def isValid(su, num, pos):
    row, col = pos

    # check row 
    for c in range(len(su[row])):
        if su[row][c] == num and c != col:
            return False

    # check column
    for r in range(len(su)):
        if su[r][col] == num and r != row:
            return False

    # check 'box'
    box_r = row // 3
    box_c = col // 3

    for r in range(box_r * 3, (box_r + 1) * 3):
        for c in range(box_c * 3, (box_c + 1) * 3):
            if su[r][c] == num and (r, c) != pos:
                return False

    return True

# Recursive solver function
def auto_solve(su):
    pos = isEmpty(su)
    if not pos:
        return True
    else:
        row, col = pos

    for i in range(1, len(su)+1):
        if isValid(su, i, (row, col)):
            su[row][col] = i

            print_su(su)

            if auto_solve(su):
                return True

            su[row][col] = 0

    return False

input_su()
print_su(su)
# Wait for user to start solving        
print("Press <Enter> to start solving.")
enter = input()
# Record the start time
start_time = datetime.datetime.now()
auto_solve(su)
# Record the end time
end_time = datetime.datetime.now()
# Print answer and elapsed time
print("\n*********************************************\n")
print("Ans:")
print_su(su)
print("Elapsed time: ", end_time - start_time)