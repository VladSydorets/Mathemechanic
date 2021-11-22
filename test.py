board = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]




board_len = len(board)

solved = [[1 for x in range(board_len)] for y in range(board_len)]

num_elemens = board_len*board_len

counter=0

for i in range(board_len):
    for j in range(board_len):
        if solved[i][j] == 1:
            counter += 1
    if counter == num_elemens:
        pass
# print(board_len)

# visited = [[0 for x in range(board_len)] for y in range(board_len)]

# print(visited)

# def is_cell_valid(board_len, x_coord, y_coord):
#     if (x_coord < 0 or y_coord < 0) or (x_coord >= board_len or y_coord >= board_len):
#         return False
#     else: 
#         return True

# def is_solved():
#     pass

# def dfs(board, x, y):
#     board_len = len(board)

#     # visited = [[0 for x in range(board_len)] for y in range(board_len)] initialize the 2d array before calling the dfs algorithm function

#     visited[x][y] = 1

#     print(f"Visited: {x}, {y}")

#     if is_cell_valid(board_len, x-1, y) and visited[x-1][y] != 1:#up
#         dfs(board, x-1, y)
#     if is_cell_valid(board_len, x, y+1) and visited[x][y+1] != 1:#right
#         dfs(board, x, y+1)
#     if is_cell_valid(board_len, x+1, y) and visited[x+1][y] != 1:#down
#         dfs(board, x+1, y)
#     if is_cell_valid(board_len, x, y-1) and visited[x][y-1] != 1:#left
#         dfs(board, x, y-1)


# dfs(board, 0, 0)