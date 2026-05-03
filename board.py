"""
Rules :

1.Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.

2.Any live cell with two or three live neighbours lives on to the next generation.

3.Any live cell with more than three live neighbours dies, as if by overpopulation.

4.Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

"""
from board_states import BoardState
class GameOfLife:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    def __init__(self, rows, cols):
        self.row = rows
        self.columns = cols

    
    def create_board(self):
        self.board = [[BoardState.DEAD  for column in range(self.columns)] for row in range(self.row)]
    
    def fetch_color(self,row, col):
        cell = self.board[row][col]
        if cell == BoardState.ALIVE:
            return self.WHITE, self.BLACK
        return self.BLACK, self.WHITE
    
    def change_cell_state(self, row, col):
        self.board[col][row] = BoardState.ALIVE if self.board[col][row] == BoardState.DEAD else BoardState.DEAD

    def check_cell_index_validity(self, row, col):
        return 0<=row<self.row and 0<=col<self.columns

    def check_cell_alive(self,row,col):
        if not self.check_cell_index_validity(row, col):
            return False
        return self.board[row][col] == BoardState.ALIVE
    
    def return_num_live_neighbours(self,row,col):
        live_neighbours = 0
        row_directions = [-1,0,1]
        column_directions = [-1,0,1]
        for row_direction in row_directions:
            for column_direction in column_directions:
                if row_direction == 0 and column_direction == 0:
                    continue
                if self.check_cell_alive(row+row_direction, col+column_direction):
                    live_neighbours+=1
        return live_neighbours
    
    def can_dead_cell_become_alive(self,row,col):
        return BoardState.ALIVE if self.return_num_live_neighbours(row,col) == 3 else BoardState.DEAD
    
    def fate_of_live_cell_in_next_generation(self,row,col):
        if self.return_num_live_neighbours(row,col) < 2 or self.return_num_live_neighbours(row,col) > 3:
            return BoardState.DEAD
        return BoardState.ALIVE    

    def apply_game_of_life_algorithm(self):
        new_board = [[BoardState.DEAD for column in range(self.columns)] for row in range(self.row)]
        for row in range(self.row):
            for col in range(self.columns):
                if(self.board[row][col] == BoardState.DEAD):
                    new_board[row][col] = self.can_dead_cell_become_alive(row,col)
                    continue
                new_board[row][col] = self.fate_of_live_cell_in_next_generation(row,col)
        return new_board

  
    def play_game_of_life(self):
        next_generation_board = self.apply_game_of_life_algorithm()
        self.board = next_generation_board
        print("Next Generation Generated")