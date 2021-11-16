import pygame
import sys

from config import consts
from draw_grid import draw_grid
import board_reader

def sum_board():

    row_sum=[]
    col_sum=[]

    # Counts the sum of the row
    for row in range(len(board_reader.board)):
        temp_sum=0
        for col in range(len(board_reader.board)):
            if board_reader.board_status[row][col]:
                temp_sum += board_reader.board[row][col]
        row_sum.append(temp_sum)
        
    # Counts the sum of the column
    for col in range(len(board_reader.board)):
        temp_sum=0
        for row in range(len(board_reader.board)):
            if board_reader.board_status[row][col]:
                temp_sum += board_reader.board[row][col]
        col_sum.append(temp_sum)

    return row_sum, col_sum

if __name__ == "__main__":
    pygame.init()

    board_len=len(board_reader.board[0])

    game_font=pygame.font.SysFont(consts.FONT_TYPE, consts.FONT_SIZE)

    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = consts.SCREEN_WIDTH/(board_len)-(consts.MARGIN*board_len+3)
    HEIGHT = consts.SCREEN_HEIGHT/(board_len)-(consts.MARGIN*board_len+3)

    # Offcast needed to draw the grid
    empty_cell_width=WIDTH*2
    empty_cell_height=HEIGHT*2

    screen=pygame.display.set_mode([consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT])
    pygame.display.set_caption("Mathemechanic")
    screen.fill(consts.BG_COLOR)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + consts.MARGIN)
                row = pos[1] // (HEIGHT + consts.MARGIN)
                if (row > 1 and column > 1) and (row < 8 and column < 8):
                    row_coords = int(row-2)
                    col_coords = int(column-2)

                    # Degen code
                    if board_reader.board_status[row_coords][col_coords]:
                        board_reader.board_status[row_coords][col_coords] = False
                    elif board_reader.board_status[row_coords][col_coords] == False:
                        board_reader.board_status[row_coords][col_coords] = True
        
        row_sum, col_sum = sum_board()
        # Call the function to draw the grid
        draw_grid(
            screen, 
            board_len, 
            WIDTH, 
            HEIGHT, 
            empty_cell_height, 
            empty_cell_width, 
            game_font,
            row_sum, 
            col_sum
        )

        pygame.display.update()

