board = [
    [1,1,9,6,4,9],
    [8,5,4,8,1,1],
    [7,7,1,8,3,4],
    [6,9,1,5,3,5],
    [8,7,6,8,9,2],
    [9,7,6,7,6,6]
]

COLUMN_GOAL = [32, 15, 11, 26, 19, 22]

ROW_GOAL = [21, 13, 20, 11, 26, 34]

# Initialize 2D-array for status of the board. It can be either True or False
board_status = [[0 for x in range(len(board))] for y in range(len(board))] 

for i in range(len(board)):
    for j in range(len(board)):
        board_status[i][j]=True