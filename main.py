import pygame
import sys

from pygame.constants import K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN, QUIT

from config import consts
from draw_grid import draw_grid

# read_board() reads the board
def read_board(level):
    map_path = "maps/map-" + str(level) + ".txt" 

    with open(map_path) as textFile:
        board = [line.strip().split(',') for line in textFile]

    # convert str to int
    board=[list(map(int,i)) for i in board]
    board_size=len(board)

    # the last two rows of the .txt file are the target columns and rows sum
    column_goal=board[board_size-2]
    row_goal=board[board_size-1]
    # remove the last two rows
    board=board[:board_size-2]

    # 2D-array for status of the board
    board_status = [[0 for x in range(len(board))] for y in range(len(board))] 

    # put True by default, instead of 0
    for i in range(len(board)):
        for j in range(len(board)):
            board_status[i][j]=True

    return board, board_size, column_goal, row_goal, board_status

def row_sum(board, board_status):
    row_sum=[]
    # Counts the sum of the row
    for row in range(len(board)):
        temp_sum=0
        for col in range(len(board)):
            if board_status[row][col]:
                temp_sum += board[row][col]
        row_sum.append(temp_sum)

    return row_sum


def col_sum(board, board_status):
    col_sum=[]
    # Counts the sum of the column
    for col in range(len(board)):
        temp_sum=0
        for row in range(len(board)):
            if board_status[row][col]:
                temp_sum += board[row][col]
        col_sum.append(temp_sum)

    return col_sum

def main_menu():

    while True:

        mx,my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(200, 100, 150, 50)
        button_2 = pygame.Rect(200, 200, 150, 50)
        button_3 = pygame.Rect(200, 300, 150, 50)
        button_4 = pygame.Rect(200, 400, 150, 50)
        button_5 = pygame.Rect(200, 500, 150, 50)

        main_text=(pygame.font.SysFont(consts.FONT_TYPE, consts.FONT_SIZE)).render("Choose difficulty", True, consts.WHITE_FONT_COLOR)
        text_1=(pygame.font.SysFont(consts.FONT_TYPE, consts.FONT_SIZE)).render("5x5", True, consts.WHITE_FONT_COLOR)
        text_2=(pygame.font.SysFont(consts.FONT_TYPE, consts.FONT_SIZE)).render("6x6", True, consts.WHITE_FONT_COLOR)
        text_3=(pygame.font.SysFont(consts.FONT_TYPE, consts.FONT_SIZE)).render("7x7", True, consts.WHITE_FONT_COLOR)
        text_4=(pygame.font.SysFont(consts.FONT_TYPE, consts.FONT_SIZE)).render("8x8", True, consts.WHITE_FONT_COLOR)
        text_5=(pygame.font.SysFont(consts.FONT_TYPE, consts.FONT_SIZE)).render("9x9", True, consts.WHITE_FONT_COLOR)

        if button_1.collidepoint((mx, my)):
            if click:
                screen.fill(consts.BG_COLOR)
                game(1)
        if button_2.collidepoint((mx, my)):
            if click:
                screen.fill(consts.BG_COLOR)
                game(2)
        if button_3.collidepoint((mx, my)):
            if click:
                screen.fill(consts.BG_COLOR)
                game(3)
        if button_4.collidepoint((mx, my)):
            if click:
                screen.fill(consts.BG_COLOR)
                game(4)
        if button_5.collidepoint((mx, my)):
            if click:
                screen.fill(consts.BG_COLOR)
                game(5)

        pygame.draw.rect(screen, consts.FONT_COLOR_OFF, button_1)
        pygame.draw.rect(screen, consts.FONT_COLOR_OFF, button_2)
        pygame.draw.rect(screen, consts.FONT_COLOR_OFF, button_3)
        pygame.draw.rect(screen, consts.FONT_COLOR_OFF, button_4)
        pygame.draw.rect(screen, consts.FONT_COLOR_OFF, button_5)

        screen.blit(main_text, ((consts.SCREEN_WIDTH/2 - main_text.get_rect().width/2) - 10, 50))
        screen.blit(text_1, ((consts.SCREEN_WIDTH/2 - text_1.get_rect().width/2) - 20, 110))
        screen.blit(text_2, ((consts.SCREEN_WIDTH/2 - text_2.get_rect().width/2 - 20), 210))
        screen.blit(text_3, ((consts.SCREEN_WIDTH/2 - text_3.get_rect().width/2 - 20), 310))
        screen.blit(text_4, ((consts.SCREEN_WIDTH/2 - text_4.get_rect().width/2 - 20), 410))
        screen.blit(text_5, ((consts.SCREEN_WIDTH/2 - text_5.get_rect().width/2 - 20), 510))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
    

def game(level):
    running = True

    board, board_size, column_goal, row_goal, board_status = read_board(level)

    # This sets the WIDTH and HEIGHT of each grid location
    board_len=len(board[0])
    WIDTH = (consts.SCREEN_WIDTH-consts.MARGIN*board_size)/(board_len+2)
    HEIGHT = (consts.SCREEN_HEIGHT-consts.MARGIN*board_size)/(board_len+2)

    # Offset needed to draw the grid
    empty_cell_width=WIDTH*2
    empty_cell_height=HEIGHT*2

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + consts.MARGIN)
                row = pos[1] // (HEIGHT + consts.MARGIN)
                if (row > 1 and column > 1) and (row < board_size and column < board_size):
                    row_coords = int(row-2)
                    col_coords = int(column-2)

                    # Degen code
                    if board_status[row_coords][col_coords]:
                        board_status[row_coords][col_coords] = False
                    elif board_status[row_coords][col_coords] == False:
                        board_status[row_coords][col_coords] = True

        row_summed = row_sum(board, board_status)
        col_summed = col_sum(board, board_status)

        visited = [[0 for x in range(board_len)] for y in range(board_len)]
        solved = [[0 for x in range(board_len)] for y in range(board_len)]

        dfs(board, 0, 0, visited, solved, row_summed, col_summed, column_goal, row_goal)
        # Call the function to draw the grid
        draw_grid(
                screen, 
                board_len, 
                WIDTH, 
                HEIGHT, 
                empty_cell_height, 
                empty_cell_width, 
                game_font,
                row_summed, 
                col_summed,
                column_goal, 
                row_goal,
                board,
                board_status
        )

        pygame.display.update()

    screen.fill(consts.BG_COLOR)

# is_cell_valid() checks if the cell's coordinates are not out of board
def is_cell_valid(board_len, x_coord, y_coord):
    if (x_coord < 0 or y_coord < 0) or (x_coord >= board_len or y_coord >= board_len):
        return False
    else: 
        return True

# is_solved() checks if the cell is solved
def is_solved(solved, row_summed, col_summed, column_goal, row_goal, x, y):
    if row_summed[x] == row_goal[x] and col_summed[y] == column_goal[y]:
        solved[x][y] = 1
    return solved

# recursive dfs algorithm
def dfs(board, x, y, visited, solved, row_summed, col_summed, column_goal, row_goal):
    board_len = len(board)

    # change the value of the visited[][] to 1 if the cell has been visited
    visited[x][y] = 1

    # check if the board is solved
    solved = is_solved(solved, row_summed, col_summed, column_goal, row_goal, x, y)

    # if the cell coordinates are valid(not out of the board) and the cell hasn't been visited then move to the next cell
    if is_cell_valid(board_len, x-1, y) and visited[x-1][y] != 1:#up
        dfs(board, x-1, y, visited, solved, row_summed, col_summed, column_goal, row_goal)
    if is_cell_valid(board_len, x, y+1) and visited[x][y+1] != 1:#right
        dfs(board, x, y+1, visited, solved, row_summed, col_summed, column_goal, row_goal)
    if is_cell_valid(board_len, x+1, y) and visited[x+1][y] != 1:#down
        dfs(board, x+1, y, visited, solved, row_summed, col_summed, column_goal, row_goal)
    if is_cell_valid(board_len, x, y-1) and visited[x][y-1] != 1:#left
        dfs(board, x, y-1, visited, solved, row_summed, col_summed, column_goal, row_goal)

    # count the number of elements on the board
    num_elemens = board_len*board_len

    # set counter to 0
    counter=0

    # if the board is solved, then all of its values should be equal to 1
    for i in range(board_len):
        for j in range(board_len):
            if solved[i][j] == 1:
                counter += 1
        if counter == num_elemens:
            print("GG")
            print(solved)
            exit()        

if __name__ == "__main__":
    pygame.init()

    game_font=pygame.font.SysFont(consts.FONT_TYPE, consts.FONT_SIZE_GOAL)

    screen=pygame.display.set_mode([consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT])
    pygame.display.set_caption("Mathemechanic")
    screen.fill(consts.BG_COLOR)

    click = False

    main_menu()