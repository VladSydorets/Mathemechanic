# def read_bord(level):
#     map_path = "maps/map-" + level + ".txt" 

#     with open(map_path) as textFile:
#         board = [line.strip().split(',') for line in textFile]

#     board=[list(map(int,i)) for i in board]
#     board_size=len(board)

#     column_goal=board[board_size-2]
#     row_goal=board[board_size-1]
#     board=board[:board_size-2]

#     # Initialize 2D-array for status of the board. It can be either True or False
#     board_status = [[0 for x in range(len(board))] for y in range(len(board))] 

#     for i in range(len(board)):
#         for j in range(len(board)):
#             board_status[i][j]=True

#     # return board, board_size, column_goal, row_goal, board_status