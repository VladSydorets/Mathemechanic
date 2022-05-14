from consts import *

class Board:
    def __init__(self, pygame) -> None:
        self.pygame=pygame
        self.board_len=0 # the length of the board
        self.board_size=0 # the size of the board + target col and row values
        self.cell_width=0 # width of the cell
        self.cell_height=0 # height of the cell
        self.empty_cell_height=0 
        self.empty_cell_width=0
        self.count_operations=0 # the number of operations the algorithm took to solve the board
        self.start_time = 0 # the time it took the algorithm to solve the board
        self.game_font=self.pygame.font.SysFont(FONT_TYPE, FONT_SIZE) # the font
        self.row_summed=[] # the sum of the each row
        self.col_summed=[] # the sum of he each column
        self.column_goal=[] # target values for the columns
        self.row_goal=[] # target values for the rows
        self.board=[] # 2D array for the board
        self.board_status=[] # 2d array, True or False to display the cells in pygame GUI
        self.domain=[] # 2D array (for forward checking)

    def read_board(self, level):
        # Path to the map
        map_path = "maps/map-" + str(level) + ".txt" 

        # Read the content of the map file
        with open(map_path) as textFile:
            self.board = [line.strip().split(',') for line in textFile]

        # Convert str to int
        self.board=[list(map(int,i)) for i in self.board]
        # Initial board size (grid + 2 rows containing target row and goal values)
        self.board_size=len(self.board)

        # The last two rows of the .txt file are the target columns and rows sum
        self.column_goal=self.board[self.board_size-2]
        self.row_goal=self.board[self.board_size-1]
        # Remove the last two rows
        self.board=self.board[:self.board_size-2]

        self.board_len = len(self.board)

        # 2D-array for status of the board
        self.board_status = [[True for x in range(len(self.board))] for y in range(len(self.board))] 

        # 2D-array needed for forward checking
        self.domain = [[True for x in range(len(self.board))] for y in range(len(self.board))]

    # The method that counts the sum of a row needed for dfs algorithm
    def row_sum(self):
        self.row_summed = []
        # Counts the sum of the row
        for row in range(len(self.board)):
            temp_sum=0
            for col in range(len(self.board)):
                if self.board_status[row][col]:
                    temp_sum += self.board[row][col]
            self.row_summed.append(temp_sum)

    # The method that counts the sum of a column, needed for dfs algorithm
    def col_sum(self):
        self.col_summed = []
        # Counts the sum of the column
        for col in range(len(self.board)):
            temp_sum=0
            for row in range(len(self.board)):
                if self.board_status[row][col]:
                    temp_sum += self.board[row][col]
            self.col_summed.append(temp_sum)

    # Sets the dimensions of the cell
    def set_cell_dimensions(self):
        self.cell_width = (SCREEN_HEIGHT-MARGIN*self.board_size)/(self.board_len+2)
        self.cell_height = (SCREEN_HEIGHT-MARGIN*self.board_size)/(self.board_len+2)

        # Offset needed to draw the grid
        self.empty_cell_width=self.cell_width*2
        self.empty_cell_height=self.cell_height*2

    def draw_grid(self, screen):
        # Draw the cells for sum of rows
        for row in range(self.board_len):
            for column in range(2):
                self.pygame.draw.rect(screen,
                                SUM_CELL_COLOR,
                                [(MARGIN + self.cell_width) * column + MARGIN,
                                ((MARGIN + self.cell_height) * row + MARGIN)+self.empty_cell_height+MARGIN*2,
                                self.cell_width,
                                self.cell_height])
                
                if column == 1:
                    row_goal_cell_value=self.game_font.render(str(self.row_goal[row]), True, RED_FONT_COLOR)
                    screen.blit(row_goal_cell_value, ((((self.cell_width/2)-row_goal_cell_value.get_rect().width/2) + MARGIN) + (MARGIN+self.cell_height) * column,
                                        (self.empty_cell_height + MARGIN*3) + ((self.cell_height/2) - (row_goal_cell_value.get_rect().height/2)) + (MARGIN+self.cell_height) * row))

                if column == 0:
                    row_cell_value=self.game_font.render(str(self.row_summed[row]), True, WHITE_FONT_COLOR)
                    screen.blit(row_cell_value, (((self.cell_width/2)-row_cell_value.get_rect().width/2) + MARGIN,
                                        (self.empty_cell_height + MARGIN*3) + ((self.cell_height/2) - (row_cell_value.get_rect().height/2)) + (MARGIN+self.cell_height) * row
                                    ))


        # Draw the cells for sum of columns
        for row in range(2):
            for column in range(self.board_len):
                self.pygame.draw.rect(screen,
                                SUM_CELL_COLOR,
                                [((MARGIN + self.cell_width) * column + MARGIN)+self.empty_cell_width+MARGIN*2,
                                (MARGIN + self.cell_height) * row + MARGIN,
                                self.cell_width,
                                self.cell_height])

                if row == 1:
                    col_goal_cell_value=self.game_font.render(str(self.column_goal[column]), True, RED_FONT_COLOR)
                    screen.blit(col_goal_cell_value, ((self.empty_cell_height + MARGIN*3) + ((self.cell_width/2) - (col_goal_cell_value.get_rect().width/2)) + (MARGIN+self.cell_width) * column,
                                                                ((self.cell_height/2)-col_goal_cell_value.get_rect().height/2) + (MARGIN+self.cell_height) * row))
                if row == 0:
                    col_cell_value=self.game_font.render(str(self.col_summed[column]), True, WHITE_FONT_COLOR)
                    screen.blit(col_cell_value, ((self.empty_cell_height + MARGIN*3) + ((self.cell_width/2) - (col_cell_value.get_rect().width/2)) + (MARGIN+self.cell_width) * column,
                                                ((self.cell_height/2)-col_cell_value.get_rect().height/2) + MARGIN))

        # Draw the grid
        for row in range(self.board_len):
            for column in range(self.board_len):
                if self.board_status[row][column] == True:
                    cell_color=CELL_COLOR
                    font_color=WHITE_FONT_COLOR
                else:
                    cell_color=CELL_COLOR_OFF
                    font_color=FONT_COLOR_OFF

                # Draw rectangles for the cells
                self.pygame.draw.rect(screen,
                                cell_color,
                                [((MARGIN + self.cell_width) * column + MARGIN)+self.empty_cell_width+MARGIN*2,
                                ((MARGIN + self.cell_height) * row + MARGIN)+self.empty_cell_height+MARGIN*2,
                                self.cell_width,
                                self.cell_height])
                self.pygame.draw.rect(screen,
                                BORDER_COLOR,
                                [((MARGIN + self.cell_width) * column + MARGIN)+self.empty_cell_width+MARGIN*2,
                                ((MARGIN + self.cell_height) * row + MARGIN)+self.empty_cell_height+MARGIN*2,
                                self.cell_width,
                                self.cell_height], width=1, border_radius=5)
                # Render values 
                cell_value=(self.pygame.font.SysFont(FONT_TYPE, FONT_SIZE)).render(str(self.board[row][column]), True, font_color)
                screen.blit(cell_value, ((self.empty_cell_width + MARGIN*3) + ((self.cell_width/2) - (col_cell_value.get_rect().width/2)) + (MARGIN+self.cell_width) * column,
                                (self.empty_cell_height + MARGIN*3) + ((self.cell_height/2) - (col_cell_value.get_rect().height/2)) + (MARGIN+self.cell_height) * row))
