import pygame
import sys

import board_reader

from config import consts
import board_reader

def draw_grid(screen, board_len, WIDTH, HEIGHT, empty_cell_height, empty_cell_width, game_font, row_sum, col_sum):
    # Draw the cells for sum of rows
    for row in range(board_len):
        for column in range(2):
            pygame.draw.rect(screen,
                            consts.SUM_CELL_COLOR,
                            [(consts.MARGIN + WIDTH) * column + consts.MARGIN,
                            ((consts.MARGIN + HEIGHT) * row + consts.MARGIN)+empty_cell_height+consts.MARGIN*2,
                            WIDTH,
                            HEIGHT])
            
            if column == 0:
                row_goal_cell_value=game_font.render(str(board_reader.ROW_GOAL[row]), True, consts.FONT_COLOR)
                screen.blit(row_goal_cell_value, (((consts.MARGIN + WIDTH) * column + consts.MARGIN + consts.FONT_SIZE/2),
                                ((consts.MARGIN + HEIGHT) * row + consts.MARGIN*3)+empty_cell_height + consts.FONT_SIZE/2))
            
            if column == 1:
                row_cell_value=game_font.render(str(row_sum[row]), True, consts.FONT_COLOR)
                screen.blit(row_cell_value, (((consts.MARGIN + WIDTH) * column + consts.MARGIN + consts.FONT_SIZE/2),
                                ((consts.MARGIN + HEIGHT) * row + consts.MARGIN*3)+empty_cell_height + consts.FONT_SIZE/2))


    # Draw the cells for sum of columns
    for row in range(2):
        for column in range(board_len):
            pygame.draw.rect(screen,
                            consts.SUM_CELL_COLOR,
                            [((consts.MARGIN + WIDTH) * column + consts.MARGIN)+empty_cell_width+consts.MARGIN*2,
                            (consts.MARGIN + HEIGHT) * row + consts.MARGIN,
                            WIDTH,
                            HEIGHT])

            if row == 0:
                col_goal_cell_value=game_font.render(str(board_reader.COLUMN_GOAL[column]), True, consts.FONT_COLOR)
                screen.blit(col_goal_cell_value, (((consts.MARGIN + WIDTH) * column + consts.MARGIN *3 + empty_cell_width + consts.FONT_SIZE/2),
                                ((consts.MARGIN + HEIGHT) * row + consts.MARGIN) + consts.FONT_SIZE/2))

            if row == 1:
                col_cell_value=game_font.render(str(col_sum[column]), True, consts.FONT_COLOR)
                screen.blit(col_cell_value, (((consts.MARGIN + WIDTH) * column + consts.MARGIN *3 + empty_cell_width + consts.FONT_SIZE/2),
                                ((consts.MARGIN + HEIGHT) * row + consts.MARGIN) + consts.FONT_SIZE/2))

    # Draw the grid
    for row in range(board_len):
        for column in range(board_len):
            if board_reader.board_status[row][column] == True:
                cell_color=consts.CELL_COLOR
                font_color=consts.FONT_COLOR
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
            cell_value=game_font.render(str(board_reader.board[row][column]), True, font_color)
            screen.blit(cell_value, (((consts.MARGIN + WIDTH) * column + consts.MARGIN*4)+empty_cell_width+consts.FONT_SIZE/2,
                            ((consts.MARGIN + HEIGHT) * row + consts.MARGIN*3)+empty_cell_height+consts.FONT_SIZE/2))
