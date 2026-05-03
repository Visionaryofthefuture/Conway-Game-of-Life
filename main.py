import pygame
from board import GameOfLife
import time 
ROW = 15
COLUMN = 12

pygame.init()
screen_height = 1000
screen_width = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("GAME OF LIFE")
button_rect = pygame.Rect(150, 120, 100, 50)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.SysFont("Arial", 24)
ROW_SIZE = screen_height // ROW
COLUMN_SIZE = screen_width // COLUMN

game_of_life = GameOfLife(ROW, COLUMN)
game_of_life.create_board()

def draw_board():
    for row in range(ROW):
        for col in range(COLUMN):
            box_color , border_color = game_of_life.fetch_color(row, col)
            pygame.draw.rect(
                screen,
                box_color,
                ( row * ROW_SIZE, col * COLUMN_SIZE,ROW_SIZE, COLUMN_SIZE),
            )
            pygame.draw.rect(
                screen,
                border_color,
                ( row * ROW_SIZE, col * COLUMN_SIZE,ROW_SIZE, COLUMN_SIZE),
                2
            )

while True:
    screen.fill(WHITE)
    draw_board()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x , mouse_y = pygame.mouse.get_pos()
            col , row = mouse_x // ROW_SIZE, mouse_y // COLUMN_SIZE
            game_of_life.change_cell_state(row, col)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                while True:
                    game_of_life.play_game_of_life()
                    draw_board()
                    pygame.display.update()
                    time.sleep(2)
    pygame.display.update()

