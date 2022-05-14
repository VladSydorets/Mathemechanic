import pygame
import sys
import time

from pygame.constants import K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN, QUIT

from consts import *
from Board import Board

# The main menu function that displays the possible grid sizes
def main_menu():
    screen.fill(BG_COLOR)

    while True:
        # Get mouse position
        mx,my = pygame.mouse.get_pos()

        # Buttons for different grid sizes
        button_1 = pygame.Rect(SCREEN_WIDTH/3+30, 100, 150, 50)
        button_2 = pygame.Rect(SCREEN_WIDTH/3+30, 200, 150, 50)
        button_3 = pygame.Rect(SCREEN_WIDTH/3+30, 300, 150, 50)
        button_4 = pygame.Rect(SCREEN_WIDTH/3+30, 400, 150, 50)
        button_5 = pygame.Rect(SCREEN_WIDTH/3+30, 500, 150, 50)

        # Text variables
        main_text=(pygame.font.SysFont(FONT_TYPE, FONT_SIZE)).render("Choose the grid", True, WHITE_FONT_COLOR)
        text_1=(pygame.font.SysFont(FONT_TYPE, FONT_SIZE)).render("3x3", True, WHITE_FONT_COLOR)
        text_2=(pygame.font.SysFont(FONT_TYPE, FONT_SIZE)).render("4x4", True, WHITE_FONT_COLOR)
        text_3=(pygame.font.SysFont(FONT_TYPE, FONT_SIZE)).render("5x5", True, WHITE_FONT_COLOR)
        text_4=(pygame.font.SysFont(FONT_TYPE, FONT_SIZE)).render("6x6", True, WHITE_FONT_COLOR)
        text_5=(pygame.font.SysFont(FONT_TYPE, FONT_SIZE)).render("7x7", True, WHITE_FONT_COLOR)

        # If the button is clicked the proceed to the game menu
        if button_1.collidepoint((mx, my)):
            if click:
                screen.fill(BG_COLOR)
                game(1)
        if button_2.collidepoint((mx, my)):
            if click:
                screen.fill(BG_COLOR)
                game(2)
        if button_3.collidepoint((mx, my)):
            if click:
                screen.fill(BG_COLOR)
                game(3)
        if button_4.collidepoint((mx, my)):
            if click:
                screen.fill(BG_COLOR)
                game(4)
        if button_5.collidepoint((mx, my)):
            if click:
                screen.fill(BG_COLOR)
                game(5)

        # Render buttons
        pygame.draw.rect(screen, FONT_COLOR_OFF, button_1)
        pygame.draw.rect(screen, FONT_COLOR_OFF, button_2)
        pygame.draw.rect(screen, FONT_COLOR_OFF, button_3)
        pygame.draw.rect(screen, FONT_COLOR_OFF, button_4)
        pygame.draw.rect(screen, FONT_COLOR_OFF, button_5)

        # Render text
        screen.blit(main_text, ((SCREEN_WIDTH/2 - main_text.get_rect().width/2) - 10, 50))
        screen.blit(text_1, ((SCREEN_WIDTH/2 - text_1.get_rect().width/2) - 20, 110))
        screen.blit(text_2, ((SCREEN_WIDTH/2 - text_2.get_rect().width/2 - 20), 210))
        screen.blit(text_3, ((SCREEN_WIDTH/2 - text_3.get_rect().width/2 - 20), 310))
        screen.blit(text_4, ((SCREEN_WIDTH/2 - text_4.get_rect().width/2 - 20), 410))
        screen.blit(text_5, ((SCREEN_WIDTH/2 - text_5.get_rect().width/2 - 20), 510))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
    
# The game function    
def game(level):
    running = True

    board.read_board(level)
    board.set_cell_dimensions()

    while running:
        # Update the rows and columns values
        board.row_sum()
        board.col_sum()
        board.draw_grid(screen)

        mx,my = pygame.mouse.get_pos()

        # Buttons for the algorithms
        dfs_btn = pygame.Rect(620, 200, 150, 50)
        back_btn = pygame.Rect(620, 300, 150, 50)
        frwrd_btn = pygame.Rect(620, 400, 150, 50)

        # Render text
        dfs_text=(pygame.font.SysFont(FONT_TYPE, FONT_SIZE)).render("DFS", True, WHITE_FONT_COLOR)
        back_text=(pygame.font.SysFont(FONT_TYPE, FONT_SIZE)).render("Backtrack", True, WHITE_FONT_COLOR)
        frwrd_text=(pygame.font.SysFont(FONT_TYPE, FONT_SIZE)).render("Fwd Check", True, WHITE_FONT_COLOR)

        # If the button is clicked then run the algorithm
        if dfs_btn.collidepoint((mx, my)):
            if click:
                print("DFS is clicked!")
                board.start_time = time.time()
                visited = [[0 for x in range(board.board_len)] for y in range(board.board_len)]
                solve_board(0, 0, visited)                
        if back_btn.collidepoint((mx, my)):
            if click:
                print("Backtracking is clicked!")
                board.start_time = time.time()
                if solve(board.board, board.row_goal, board.column_goal):
                    finished()                
        if frwrd_btn.collidepoint((mx, my)):
            if click:
                print("Forward checking is clicked!")
                board.start_time = time.time()
                if solve_frwrd_check():
                    print(board.board)
                    finished()              

        pygame.draw.rect(screen, FONT_COLOR_OFF, dfs_btn)
        pygame.draw.rect(screen, FONT_COLOR_OFF, back_btn)
        pygame.draw.rect(screen, FONT_COLOR_OFF, frwrd_btn)

        screen.blit(dfs_text, ((720 - dfs_text.get_rect().width/2) - 20, 210))
        screen.blit(back_text, ((720 - back_text.get_rect().width/2 - 20), 310))
        screen.blit(frwrd_text, ((720 - frwrd_text.get_rect().width/2 - 20), 410))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()            

    screen.fill(BG_COLOR)

# The finished function will run when the algorithm found the solution
# It will display in the console the number of operations and the time it takes for the algorithm to find the correct solution
def finished():
    print("Solved!")
    print("Number of operations -",board.count_operations)
    print(f"Time: {time.time() - board.start_time}s")
    while True:
        board.row_sum()
        board.col_sum()
        pygame.display.update()
        board.draw_grid(screen)

        board.count_operations=0
        board.draw_grid(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
        pygame.display.update()

#                   DFS ALGORITHM               #

# is_cell_valid() checks if the cell's coordinates are not out of board
def is_cell_valid(x_coord, y_coord):
    if (x_coord < 0 or y_coord < 0) or (x_coord >= board.board_len or y_coord >= board.board_len):
        return False
    return True

# The function checks if the board is solved
# Returns True if it is solved, returns False otherwise
def is_solved():
    solved = [[0 for x in range(board.board_len)] for y in range(board.board_len)]

    for x in range(board.board_len):
        for y in range(board.board_len):
            if is_cell_correct(x,y):
                solved[x][y] = 1

    # Count the number of elements in the board
    num_elemens = board.board_len*board.board_len
    counter=0

    # The board is solved when all of the values in the solved array are 1's
    for i in range(board.board_len):
        for j in range(board.board_len):
            if solved[i][j] == 1:
                counter += 1
        if counter == num_elemens:
            return True

    return False  

# The function to check if the cell is correct
def is_cell_correct(x, y):
    board.row_sum()
    board.col_sum()
    counter = 0

    for y in range(board.board_len):
        if board.row_summed[y] == board.row_goal[y] and board.col_summed[y] == board.column_goal[y]:
            counter += 1
    
    if counter == len(board.row_goal):
        return True

    return False

# The function chooses the next cell to put the value in
def choose_cell(x,y, visited):
    for i in range(x,board.board_len):
        for j in range(y, board.board_len):
            if visited[i][j] == 0 and is_cell_valid(i,j):# if the cell is not visited and is valid => return i,j
                return i,j

    for i in range(0,board.board_len):
        for j in range(0, board.board_len):
            if visited[i][j] == 0 and is_cell_valid(i,j):
                return i,j
        
    # if it iterated througt the whole board and did not find a valid cell, return -1 to indicate that the board is full
    return -1,-1
    
# The function with the main logic of the dfs algorithm
def solve_board(x, y, visited):
    # Choose the next cell
    x,y=choose_cell(x,y,visited)

    # Update the grid at each algorithm iteration
    board.draw_grid(screen)
    pygame.display.update()

    board.count_operations += 1

    if x == -1:# if -1 is returned, it means that the algorithm reached the end of the board
        if is_solved():
            finished()
        return False

    # In the case of dfs algorithm the possible values of the board can be 0 and 1
    for i in range (2):
        if i == 1:
            board.board_status[x][y]=True
        elif i == 0:
            board.board_status[x][y]=False
        # mark the current cell as visited
        visited[x][y] = 1

        if solve_board(x,y,visited):
            return True

    # Unmark the current cell as visited and return False
    visited[x][y]=0
    return False 

#           BACKTRACKING            #

# function to sum up the rows
def all_sum(board_arr, rows):
    return all(
        target_sum == sum(row) # sum the row
        for target_sum, row in zip(rows, board_arr)
    )

# if the board is solved => return True
def solved(board_arr, rows, cols):
    return (
        all_sum(board_arr, rows) and
        all_sum(zip(*board_arr[::-1]), cols)
    )

# main logic of the backtracking algorithm
def solve(board_arr, rows, cols, x=0, y=0):
    board.row_sum()
    board.col_sum()
    pygame.display.update()
    board.draw_grid(screen)

    board.count_operations += 1

    if x >= len(board_arr): # if the end of the board is reached
        return solved(board_arr, rows, cols) # check whether it's solved or not
    elif y >= len(board_arr[x]): # if the end of the row is reached
        # if the sum of the row does not equal to the target value of the row => return False
        if sum(board_arr[x]) != rows[x]:    
            return False
        return solve(board_arr, rows, cols, x + 1, 0) # go to the next row and try to solve it
    elif sum(board_arr[x]) < rows[x]:  
        return False

    temp_value = board_arr[x][y] # store the value of the cell in the temp variable
    board_arr[x][y] = 0 # set the current cell value to 0
    board.board_status[x][y] = False # display it on the board

    if solve(board_arr, rows, cols, x, y + 1): # go and try to solve the board with this value
        return True

    board_arr[x][y] = temp_value # backtrack to the previous value
    board.board_status[x][y] = True
    return solve(board_arr, rows, cols, x, y + 1)

#               FORWARD CHECKING                    #

# forward checking function iterates through the board and tries to find the values,
# that should not be tried, because the already don't meet the requirements
def forward_check():
    temp_col= [sum(m) for m in zip(*board.board)] # sum the cols
    
    for i in range(len(temp_col)):
        if temp_col[i] == board.column_goal[i]: # if the sum of the column already is eqaul to the target value, then set all of the column values to False
            for j in range(len(board.column_goal)):
                board.domain[j][i]=False
    
    # iterate through the board and mark the cells that have already been turned off 
    for i in range(len(board.board)):
        for j in range(len(board.board)):
            if board.board[i][j] == 0:
                board.domain[i][j] = False

# main logic of the forward checking algorithm
def solve_frwrd_check(x=0, y=0):
    board.row_sum()
    board.col_sum()
    pygame.display.update()
    board.draw_grid(screen)

    board.count_operations += 1

    if x >= len(board.board):
        return solved(board.board, board.row_goal, board.column_goal) # is the board solved?
    elif y >= len(board.board[x]):
        if sum(board.board[x]) != board.row_goal[x]:
            return False
        forward_check() # if the row is correct, call the forward checking function to check for the values that can be skipped
        return solve_frwrd_check(x + 1, 0) 
    elif sum(board.board[x]) < board.row_goal[x]:
        return False

    if board.domain[x][y]:
        temp_value = board.board[x][y] 
        board.board[x][y] = 0 
        board.board_status[x][y] = False
        board.domain[x][y]=True

    if solve_frwrd_check(x, y + 1): 
        return True

    # backtrack to the previous value
    if board.domain[x][y]:
        board.board_status[x][y] = True
        board.board[x][y] = temp_value
    return solve_frwrd_check(x, y + 1) # go recursively and try again for the prev value

    
if __name__ == "__main__":
    pygame.init()
    screen=pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption("Mathemechanic")
    screen.fill(BG_COLOR)

    click = False

    board = Board(pygame)

    main_menu()