with open("maps/map-1.txt") as textFile:
    board = [line.strip().split(',') for line in textFile]

board=[list(map(int,i)) for i in board]

board_size=len(board)

COLUMN_GOAL=board[board_size-2]
ROW_GOAL=board[board_size-1]

board=board[:board_size-2]

print(board)
print(COLUMN_GOAL)
print(ROW_GOAL)

# Initialize 2D-array for status of the board. It can be either True or False
board_status = [[0 for x in range(len(board))] for y in range(len(board))] 

for i in range(len(board)):
    for j in range(len(board)):
        board_status[i][j]=True