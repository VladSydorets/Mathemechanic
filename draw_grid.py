import pygame
import sys

from config import consts

def draw_grid(screen, board_len, WIDTH, HEIGHT, empty_cell_height, empty_cell_width, game_font, row_sum, col_sum, column_goal, row_goal, board, board_status):
    # Draw the cells for sum of rows
    for row in range(board_len):
        for column in range(2):
            pygame.draw.rect(screen,
                            consts.SUM_CELL_COLOR,
                            [(consts.MARGIN + WIDTH) * column + consts.MARGIN,
                            ((consts.MARGIN + HEIGHT) * row + consts.MARGIN)+empty_cell_height+consts.MARGIN*2,
                            WIDTH,
                            HEIGHT])
            
            if column == 1:
                row_goal_cell_value=game_font.render(str(row_goal[row]), True, consts.RED_FONT_COLOR)
                screen.blit(row_goal_cell_value, ((((WIDTH/2)-row_goal_cell_value.get_rect().width/2) + consts.MARGIN) + (consts.MARGIN+HEIGHT) * column,
                                    (empty_cell_height + consts.MARGIN*3) + ((HEIGHT/2) - (row_goal_cell_value.get_rect().height/2)) + (consts.MARGIN+HEIGHT) * row))

            if column == 0:
                row_cell_value=game_font.render(str(row_sum[row]), True, consts.WHITE_FONT_COLOR)
                screen.blit(row_cell_value, (((WIDTH/2)-row_cell_value.get_rect().width/2) + consts.MARGIN,
                                    (empty_cell_height + consts.MARGIN*3) + ((HEIGHT/2) - (row_cell_value.get_rect().height/2)) + (consts.MARGIN+HEIGHT) * row
                                ))


    # Draw the cells for sum of columns
    for row in range(2):
        for column in range(board_len):
            pygame.draw.rect(screen,
                            consts.SUM_CELL_COLOR,
                            [((consts.MARGIN + WIDTH) * column + consts.MARGIN)+empty_cell_width+consts.MARGIN*2,
                            (consts.MARGIN + HEIGHT) * row + consts.MARGIN,
                            WIDTH,
                            HEIGHT])

            if row == 1:
                col_goal_cell_value=game_font.render(str(column_goal[column]), True, consts.RED_FONT_COLOR)
                screen.blit(col_goal_cell_value, ((empty_cell_height + consts.MARGIN*3) + ((WIDTH/2) - (col_goal_cell_value.get_rect().width/2)) + (consts.MARGIN+WIDTH) * column,
                                                            ((HEIGHT/2)-col_goal_cell_value.get_rect().height/2) + (consts.MARGIN+HEIGHT) * row))
            if row == 0:
                col_cell_value=game_font.render(str(col_sum[column]), True, consts.WHITE_FONT_COLOR)
                screen.blit(col_cell_value, ((empty_cell_height + consts.MARGIN*3) + ((WIDTH/2) - (col_cell_value.get_rect().width/2)) + (consts.MARGIN+WIDTH) * column,
                                            ((HEIGHT/2)-col_cell_value.get_rect().height/2) + consts.MARGIN))

    # Draw the grid
    for row in range(board_len):
        for column in range(board_len):
            if board_status[row][column] == True:
                cell_color=consts.CELL_COLOR
                font_color=consts.WHITE_FONT_COLOR
            else:
                cell_color=consts.CELL_COLOR_OFF
                font_color=consts.FONT_COLOR_OFF

            pygame.draw.rect(screen,
                            cell_color,
                            [((consts.MARGIN + WIDTH) * column + consts.MARGIN)+empty_cell_width+consts.MARGIN*2,
                            ((consts.MARGIN + HEIGHT) * row + consts.MARGIN)+empty_cell_height+consts.MARGIN*2,
                            WIDTH,
                            HEIGHT])
            pygame.draw.rect(screen,
                            consts.BORDER_COLOR,
                            [((consts.MARGIN + WIDTH) * column + consts.MARGIN)+empty_cell_width+consts.MARGIN*2,
                            ((consts.MARGIN + HEIGHT) * row + consts.MARGIN)+empty_cell_height+consts.MARGIN*2,
                            WIDTH,
                            HEIGHT], width=1, border_radius=5)
            # Render values 
            cell_value=(pygame.font.SysFont(consts.FONT_TYPE, consts.FONT_SIZE)).render(str(board[row][column]), True, font_color)
            screen.blit(cell_value, ((empty_cell_width + consts.MARGIN*3) + ((WIDTH/2) - (col_cell_value.get_rect().width/2)) + (consts.MARGIN+WIDTH) * column,
                            (empty_cell_height + consts.MARGIN*3) + ((HEIGHT/2) - (col_cell_value.get_rect().height/2)) + (consts.MARGIN+HEIGHT) * row))