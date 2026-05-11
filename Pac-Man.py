from board import board
import pygame
import math

pygame.init()

WIDTH = 900
HEIGHT = 950
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 20)
color = 'blue'
PI = math.pi

def draw_board():
    num1 = ((HEIGHT - 50)//32) 
    num2 = (WIDTH//30)
    for i in range(len(board)): #iterate through each row of the board list
        for j in range(len(board[i])): #iterate through each value in each row
            if board[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4) #(x,y) is at the center of the tile, radius 4
            if board[i][j] == 2:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10) #(x,y) is at the center of the tile, radius 10
            if board[i][j] == 3:
                pygame.draw.line(screen, color, (j * num2 + (0.5 * num2), i * num1), (j * num2 + (0.5 * num2), i * num1 + num1), 3) #starting (x,y) is at top middle of tile, ending (x,y) is at same x but bottom of tile, thickness of 3
            if board[i][j] == 4:
                pygame.draw.line(screen, color, (j * num2 , i * num1 + (0.5 * num2)), (j * num2 + num2, i * num1 + (0.5 * num1)), 3) #starting (x,y) is at side of tile, ending (x,y) is at same y but on the opposite side, thickness of 3
            if board[i][j] == 5:
                pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1], 0, PI/2, 3)
            if board[i][j] == 6:
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI/2, PI, 3)
            if board[i][j] == 7:
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], PI, 3*PI/2, 3)
            if board[i][j] == 8:
                pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3*PI/2, 2*PI, 3)
            if board[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * num2 , i * num1 + (0.5 * num2)), (j * num2 + num2, i * num1 + (0.5 * num1)), 3) #starting (x,y) is at side of tile, ending (x,y) is at same y but on the opposite side, thickness of 3

run = True
while run:
    timer.tick(60) #how fast the game runs
    screen.fill('black')
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if you exit out the game
            run = False

    pygame.display.flip() #draws it every iteration
pygame.quit()



