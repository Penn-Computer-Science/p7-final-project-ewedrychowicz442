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
player_x = 450
player_y = 663
ghost1_img = (pygame.transform.scale(pygame.image.load(f'BlueGhost_img.png'), (50, 50)))
ghost2_img = (pygame.transform.scale(pygame.image.load(f'PurpleGhost_img.png'), (50, 50)))
ghost3_img = (pygame.transform.scale(pygame.image.load(f'RedGhost_img.png'), (50, 50)))
ghost1_x = 56
ghost1_y = 58
ghost1_direction = 0
ghost2_x = 440
ghost2_y = 388
ghost2_direction = 2
ghost3_x = 440
ghost3_y = 438
ghost3_direction = 2
direction_command = 0
direction = 0
direction_command = 0
player_speed = 2
score = 0
ghost_targets = [(player_x, player_y), (player_x, player_y), (player_x, player_y)]
ghost1_box =  False
ghost2_box = False
ghost3_box = False
ghost_speed = 2
moving = False
startup_counter = 0
lives = 3

class Ghost:
    def __init__(self, x_coord, y_coord, target, speed, img, direct, box, id):
        self.x_pos = x_coord
        self.y_pos = y_coord
        self.center_x = self.x_pos + 25
        self.center_y = self.y_pos + 25
        self.target = target
        self.speed = speed
        self.img = img
        self.direct = direct
        self.in_box = box
        self.id = id
        self.turns, self.in_box = self.check_collisions()
        self.rect = self.draw()
    
    def draw(self):
        while True:
            screen.blit(self.img, (self.x_pos, self.y_pos))
            ghost_rect = pygame.rect.Rect((self.center_x - 21, self.center_y - 21), (42, 42))
            return ghost_rect
    
    def check_collisions(self):
        #R, L, U, D
        num1 = ((HEIGHT - 50) // 32)
        num2 = (WIDTH // 30)
        num3 = 14
        self.turns = [False, False, False, False]
        if self.center_x // 30 < 29:
            if board[self.center_y // num1][(self.center_x - num3) // num2] < 3 or board[self.center_y // num1][(self.center_x - num3) // num2] == 9 and (self.in_box):
                self.turns[1] = True
            if board[self.center_y // num1][(self.center_x + num3) // num2] < 3 or board[self.center_y // num1][(self.center_x + num3) // num2] == 9 and (self.in_box):
                self.turns[0] = True
            if board[(self.center_y + num3) // num1][self.center_x // num2] < 3 or board[(self.center_y + num3) // num1][self.center_x // num2] == 9 and (self.in_box):
                self.turns[3] = True
            if board[(self.center_y - num3) // num1][self.center_x // num2] < 3 or board[(self.center_y - num3) // num1][self.center_x // num2] == 9 and (self.in_box):
                self.turns[2] = True
            
            if self.direct == 2 or self.direct == 3:
                if 12 <= self.center_x % num2 <= 18:
                    if board[(self.center_y + num3) // num1][self.center_x // num2] < 3 or board[(self.center_y + num3) // num1][self.center_x // num2] == 9 and (self.in_box):
                        self.turns[3] = True
                    if board[(self.center_y - num3) // num1][self.center_x // num2] < 3 or board[(self.center_y - num3) // num1][self.center_x // num2] == 9 and (self.in_box):
                        self.turns[2] = True
                if 12 <= self.center_y % num1 <= 18:
                    if board[self.center_y // num1][(self.center_x - num2) // num2] < 3 or board[self.center_y // num1][(self.center_x - num2) // num2] == 9 and (self.in_box):
                        self.turns[1] = True
                    if board[self.center_y // num1][(self.center_x + num2) // num2] < 3 or board[self.center_y // num1][(self.center_x + num2)// num2] == 9 and (self.in_box):
                        self.turns[0] = True
            
            if self.direct == 0 or self.direct == 1:
                if 12 <= self.center_x % num2 <= 18:
                    if board[(self.center_y + num3) // num1][self.center_x // num2] < 3 or board[(self.center_y + num3) // num1][self.center_x // num2] == 9 and (self.in_box):
                        self.turns[3] = True
                    if board[(self.center_y - num3) // num1][self.center_x // num2] < 3 or board[(self.center_y - num3) // num1][self.center_x // num2] == 9 and (self.in_box):
                        self.turns[2] = True
                if 12 <= self.center_y % num1 <= 18:
                    if board[self.center_y // num1][(self.center_x - num3) // num2] < 3 or board[self.center_y // num1][(self.center_x - num3) // num2] == 9 and (self.in_box):
                        self.turns[1] = True
                    if board[self.center_y // num1][(self.center_x + num3) // num2] < 3 or board[self.center_y // num1][(self.center_x + num3)// num2] == 9 and (self.in_box):
                        self.turns[0] = True
        else:
            self.turns[0] = True
            self.turns[1] = True
        if 350 < self.x_pos < 550 and 370 < self.y_pos < 490:
            self.in_box = True
        else: 
            self.in_box = False
        return self.turns, self.in_box

    def move_ghost3(self):
        if self.direct == 0:
            if self.target[0] > self.x_pos and self.turns[0]:
                self.x_pos += self.speed
            elif not self.turns[0]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direct = 3
                    self.y_pos += self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direct = 2
                    self.y_pos -= self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direct = 1
                    self.x_pos -= self.speed
                elif self.turns[3]:
                    self.direct = 3
                    self.y_pos += self.speed
                elif self.turns[2]:
                    self.direct = 2
                    self.y_pos -= self.speed
                elif self.turns[1]:
                    self.direct = 1
                    self.x_pos -= self.speed
            elif self.turns[0]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direct = 3
                    self.y_pos += self.speed
                if self.target[1] < self.y_pos and self.turns[2]:
                    self.direct = 2
                    self.y_pos -= self.speed
                else:
                    self.x_pos += self.speed
        elif self.direct == 1:
            if self.target[1] > self.y_pos and self.turns[3]:
                self.direct = 3
            elif self.target[0] < self.x_pos and self.turns[1]:
                self.x_pos -= self.speed
            elif not self.turns[1]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direct = 3
                    self.y_pos += self.speed
                elif self.target[1] < self.y_pos and self.turns[2]:
                    self.direct = 2
                    self.y_pos -= self.speed
                elif self.target[0] > self.x_pos and self.turns[0]:
                    self.direct = 0
                    self.x_pos += self.speed
                elif self.turns[3]:
                    self.direct = 3
                    self.y_pos += self.speed
                elif self.turns[2]:
                    self.direct = 2
                    self.y_pos -= self.speed
                elif self.turns[0]:
                    self.direct = 0
                    self.x_pos += self.speed
            elif self.turns[1]:
                if self.target[1] > self.y_pos and self.turns[3]:
                    self.direct = 3
                    self.y_pos += self.speed
                if self.target[1] < self.y_pos and self.turns[2]:
                    self.direct = 2
                    self.y_pos -= self.speed
                else:
                    self.x_pos -= self.speed
        elif self.direct == 2:
            if self.target[0] < self.x_pos and self.turns[1]:
                self.direct = 1
                self.x_pos -= self.speed
            elif self.target[1] < self.y_pos and self.turns[2]:
                self.y_pos -= self.speed
            elif not self.turns[2]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direct = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direct = 1
                    self.x_pos -= self.speed
                elif self.target[1] > self.y_pos and self.turns[3]:
                    self.direct = 3
                    self.y_pos += self.speed
                elif self.turns[3]:
                    self.direct = 3
                    self.y_pos += self.speed
                elif self.turns[1]:
                    self.direct = 1
                    self.x_pos -= self.speed
                elif self.turns[0]:
                    self.direct = 0
                    self.x_pos += self.speed
            elif self.turns[2]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direct = 0
                    self.x_pos += self.speed
                if self.target[0] < self.x_pos and self.turns[1]:
                    self.direct = 1
                    self.x_pos -= self.speed
                else:
                    self.y_pos -= self.speed
        elif self.direct == 3:
            if self.target[1] > self.y_pos and self.turns[3]:
                self.y_pos += self.speed
            elif not self.turns[3]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direct = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direct = 1
                    self.x_pos -= self.speed
                if self.target[1] < self.y_pos and self.turns[2]:
                    self.direct = 2
                    self.y_pos -= self.speed
                elif self.turns[2]:
                    self.direct = 2
                    self.y_pos -= self.speed
                elif self.turns[1]:
                    self.direct = 1
                    self.x_pos -= self.speed
                elif self.turns[0]:
                    self.direct = 0
                    self.x_pos += self.speed
            elif self.turns[3]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direct = 0
                    self.x_pos += self.speed
                elif self.target[0] < self.x_pos and self.turns[1]:
                    self.direct = 1
                    self.x_pos -= self.speed
                elif self.target[1] > self.y_pos and self.turns[3]:
                    self.direct = 3
                    self.y_pos += self.speed
                elif self.turns[3]:
                    self.direct = 3
                    self.y_pos += self.speed
                elif self.turns[1]:
                    self.direct = 1
                    self.x_pos -= self.speed
                elif self.turns[0]:
                    self.direct = 0
                    self.x_pos += self.speed
            elif self.turns[2]:
                if self.target[0] > self.x_pos and self.turns[0]:
                    self.direct = 0
                    self.x_pos += self.speed
                if self.target[0] < self.x_pos and self.turns[1]:
                    self.direct = 1
                    self.x_pos -= self.speed
                else:
                    self.y_pos += self.speed
        if self.x_pos < -30:
            self.x_pos = 900
        elif self.x_pos > 900:
            self.x_pos - 30
        return self.x_pos, self.y_pos, self.direct

def draw_random():
    score_text = font.render(f'Score: {score}', True, 'white')
    screen.blit(score_text, (10, 920)) #display the score
    for i in range(lives): #place three small pacman in bottom right to count lives
        screen.blit(pygame.transform.scale(pygame.image.load(f'player_image.png'), (35, 35)), (650 + i * 40, 915))

def check_collisions(score):
    num1 = (HEIGHT - 50) // 32
    num2 = WIDTH // 30
    if 0 < player_x < 870: #if player on the board
        if board[center_y //num1][center_x // num2] == 1: #if tile has a piece of food
            board[center_y //num1][center_x // num2] = 0 #change tile to empty square
            score += 10 #increase score by 10 each piece of food collected
    return score

def draw_board():
    num1 = ((HEIGHT - 50)//32) 
    num2 = (WIDTH//30)
    for i in range(len(board)): #iterate through each row of the board list
        for j in range(len(board[i])): #iterate through each value in each row
            if board[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4) #(x,y) is at the center of the tile, radius 4
            elif board[i][j] == 2:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10) #(x,y) is at the center of the tile, radius 10
            elif board[i][j] == 3:
                pygame.draw.line(screen, color, (j * num2 + (0.5 * num2), i * num1), (j * num2 + (0.5 * num2), i * num1 + num1), 3) #starting (x,y) is at top middle of tile, ending (x,y) is at same x but bottom of tile, thickness of 3
            elif board[i][j] == 4:
                pygame.draw.line(screen, color, (j * num2 , i * num1 + (0.5 * num2)), (j * num2 + num2, i * num1 + (0.5 * num1)), 3) #starting (x,y) is at side of tile, ending (x,y) is at same y but on the opposite side, thickness of 3
            elif board[i][j] == 5:
                pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1], 0, PI/2, 3)
            elif board[i][j] == 6:
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI/2, PI, 3)
            elif board[i][j] == 7:
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], PI, 3*PI/2, 3)
            elif board[i][j] == 8:
                pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3*PI/2, 2*PI, 3)
            elif board[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * num2 , i * num1 + (0.5 * num2)), (j * num2 + num2, i * num1 + (0.5 * num1)), 3) #starting (x,y) is at side of tile, ending (x,y) is at same y but on the opposite side, thickness of 3

def draw_player():
    player_image = (pygame.transform.scale(pygame.image.load(f'player_image.png'), (50, 50))) #load the player image and scale it to 45 by 45
    #RIGHT = 0, LEFT = 1, UP = 2, DOWN = 3
    if direction == 0:
        screen.blit(player_image, (player_x, player_y)) #starting position
    elif direction == 1:
        screen.blit(pygame.transform.flip(player_image, True, False), (player_x, player_y)) #flip pac man in the x direction
    elif direction == 2:
        screen.blit(pygame.transform.rotate(player_image, 90), (player_x, player_y)) #rotate pac man 90 degrees counterclockwise
    elif direction == 3:
        screen.blit(pygame.transform.rotate(player_image, 270), (player_x, player_y)) #rotate pac man 270 degrees counterclockwise

def check_position(center_x, center_y):
    turns = [False, False, False, False] #list of possible valid directions that the player can move in
    num1 = ((HEIGHT - 50)//32) 
    num2 = (WIDTH//30)
    num3 = 14
    #check collisions based on center x and y of player
    if center_x // 30 < 29:
        if direction == 0:
            if board[center_y // num1][(center_x - num3) // num2] < 3:
                turns[1] = True
        if direction == 1:
            if board[center_y // num1][(center_x + num3) // num2] < 3:
                turns[0] = True
        if direction == 2:
            if board[(center_y + num3) // num1][center_x // num2] < 3:
                turns[3] = True
        if direction == 3:
            if board[(center_y - num3) // num1][center_x // num2] < 3:
                turns[2] = True

        if direction == 2 or direction == 3:
            if 12 <= center_x % num2 <= 18:
                if board[(center_y + num3) // num1][center_x // num2] < 3:
                    turns[3] = True
                if board[(center_y - num3) // num1][center_x // num2] < 3:
                    turns[2] = True
            if 12 <= center_y % num1 <= 18:
                if board[center_y  // num1][(center_x - num2)// num2] < 3:
                    turns[1] = True
                if board[center_y // num1][(center_x + num2) // num2] < 3:
                    turns[0] = True

        if direction == 0 or direction == 1:
            if 12 <= center_x % num2 <= 18:
                if board[(center_y + num1) // num1][center_x // num2] < 3:
                    turns[3] = True
                if board[(center_y - num1) // num1][center_x // num2] < 3:
                    turns[2] = True
            if 12 <= center_y % num1 <= 18:
                if board[center_y  // num1][(center_x - num3)// num2] < 3:
                    turns[1] = True
                if board[center_y // num1][(center_x + num3) // num2] < 3:
                    turns[0] = True

    else:
        turns[0] = True
        turns[1] = True

    return turns

def move_player(player_x, player_y):
    #r, l, u, d
    if direction == 0 and valid_turns[0]: #if direction is right and valid turns is true at position 0, increase the player's center x value
        player_x += player_speed
    elif direction == 1 and valid_turns[1]: #if direction is left and valid turns is true at position 1, decrease the player's center x value
        player_x -= player_speed
    elif direction == 2 and valid_turns[2]: #if direction is up and valid turns is true at position 2, decrease the player's center y value
        player_y -= player_speed
    elif direction == 3 and valid_turns[3]: #if direction is down and valid turns is true at position 3, increase the player's center y value
        player_y += player_speed
    return player_x, player_y

def get_targets(ghost1_x, ghost1_y, ghost2_x, ghost2_y, ghost3_x, ghost3_y):
    if 340 < ghost1_x < 560 and 340 < ghost1_y < 500:
        ghost1_target = (400, 100)
    else:
        ghost1_target = (player_x, player_y)
    if 340 < ghost2_x < 560 and 340 < ghost2_y < 500:
        ghost2_target = (400, 100)
    else:
        ghost2_target = (player_x, player_y)
    if 340 < ghost3_x < 560 and 340 < ghost3_y < 500:
        ghost3_target = (400, 100)
    else:
        ghost3_target = (player_x, player_y)

    return[ghost1_target, ghost2_target, ghost3_target]

run = True
while run:
    timer.tick(60) #how fast the game runs
    if startup_counter < 180: #have a 3 second time period without movement at the start
        moving = False
        startup_counter += 1
    else:
        moving = True
    screen.fill('black')
    draw_board()
    draw_player()
    ghost1 = Ghost(ghost1_x, ghost1_y, ghost_targets[0], ghost_speed, ghost1_img, ghost1_direction, ghost1_box, 0)
    ghost2 = Ghost(ghost2_x, ghost2_y, ghost_targets[1], ghost_speed, ghost2_img, ghost2_direction, ghost2_box, 1)
    ghost3 = Ghost(ghost3_x, ghost3_y, ghost_targets[2], ghost_speed, ghost3_img, ghost3_direction, ghost3_box, 2)
    draw_random()
    targets = get_targets(ghost1_x, ghost1_y, ghost2_x, ghost2_y, ghost3_x, ghost3_y)
    center_x = player_x + 25
    center_y = player_y + 25
    valid_turns = check_position(center_x, center_y)
    if moving: #if moving is true move player
        player_x, player_y = move_player(player_x, player_y)
        ghost1_x, ghost1_y, ghost1_direction = ghost1.move_ghost3()
        ghost2_x, ghost2_y, ghost2_direction = ghost2.move_ghost3()
        ghost3_x, ghost3_y, ghost3_direction = ghost3.move_ghost3()
    score = check_collisions(score)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if you exit out the game
            run = False
        if event.type == pygame.KEYDOWN: #handles the moving of pac man
            if event.key == pygame.K_RIGHT:
                direction_command = 0
            if event.key == pygame.K_LEFT:
                direction_command = 1
            if event.key == pygame.K_UP:
                direction_command = 2
            if event.key == pygame.K_DOWN:
                direction_command = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and direction_command == 0:
                direction_command = direction
            if event.key == pygame.K_LEFT and direction_command == 1:
                direction_command = direction
            if event.key == pygame.K_UP and direction_command == 2:
                direction_command = direction
            if event.key == pygame.K_DOWN and direction_command == 3:
                direction_command = direction
        
    if direction_command == 0 and valid_turns[0]:
        direction = 0
    if direction_command == 1 and valid_turns[1]:
        direction = 1
    if direction_command == 2 and valid_turns[2]:
        direction = 2
    if direction_command == 3 and valid_turns[3]:
        direction = 3
    
    for i in range(4):
        if direction_command == i and valid_turns[i]:
            direction = i

    if player_x > 900:
        player_x = -47
    elif player_x < -50:
        player_x = 897

    pygame.display.flip() #draws it every iteration
pygame.quit()



