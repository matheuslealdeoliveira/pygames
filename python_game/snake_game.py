import pygame
from pygame.locals import *
import random
from time import time

#sort grid apple
def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

# #sort grid monster
# def on_grid_random_monster():
#     x = random.randint(0,590)
#     y = random.randint(0,590)
#     pos1 = ((x+10)//10 * 10, y//10 * 10)
#     pos2 = (((x+10)//10) * 10, ((y+10)//10) * 10)
#     pos3 = (x//10 * 10, ((y+10)//10) * 10)
#     monster_pos = [pos1, pos2, pos3]
#     print(monster_pos)
#     return monster_pos

#collision on apple
def collisionApple(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

#collision on body
def collisionBody(c1, c2):
    return c1 == c2

# #collision on monster
# def collisionMonster(c1, c2):
#     return c1 == c2

#collision on border
def collisionBorder(c1):
    if 0 <= c1[0] < 600 and 0 <= c1[1] < 600:
        return False
    else:
        return True

#setup variables to direction
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
game = True
speed_snake = 20
score = 4

pygame.init()

#setup screen
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake")

#setup snake
snake = [(200,200), (210,200), (220,200), (230,200), (240,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((0,255,0))

#setup apple
apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

# #setup monster
# monster_pos = ((100,100))
# monster = pygame.Surface((10,10))
# monster.fill((255, 255, 255))

#start direction
my_direction = LEFT

clock = pygame.time.Clock()

while game == True:
    clock.tick(speed_snake)
    
    for event in pygame.event.get():
        #exit game
        if event.type == QUIT:
            game = False
    
    #setup color background    
    screen.fill((0,0,0)) 

    #print apple on screen
    screen.blit(apple, apple_pos)
    
    #print snake on screen
    for pos in snake:
        screen.blit(snake_skin, pos)
    
    #change direction
    if event.type == KEYDOWN and my_direction == UP:
        if event.key == K_UP:
            my_direction = UP                    
        if event.key == K_LEFT:
            my_direction = LEFT
        if event.key == K_RIGHT:
            my_direction = RIGHT

    #change direction        
    if event.type == KEYDOWN and my_direction == DOWN:
        if event.key == K_DOWN:
            my_direction = DOWN                    
        if event.key == K_LEFT:
            my_direction = LEFT
        if event.key == K_RIGHT:
            my_direction = RIGHT

    #change direction        
    if event.type == KEYDOWN and my_direction == LEFT:
        if event.key == K_UP:
            my_direction = UP
        if event.key == K_DOWN:
            my_direction = DOWN                    
        if event.key == K_LEFT:
            my_direction = LEFT
        
    #change direction
    if event.type == KEYDOWN and my_direction == RIGHT:
        if event.key == K_UP:
            my_direction = UP
        if event.key == K_DOWN:
            my_direction = DOWN                    
        if event.key == K_RIGHT:
            my_direction = RIGHT
    
    #snake eat apple 
    if collisionApple(snake[0], apple_pos):        
        #setup new apple
        apple_pos = on_grid_random()
        #speed up
        speed_snake = speed_snake + 1
        #add score
        score = score + 1
        #add +1 in snake
        snake.append((0,0))
        
#     #print monster on screen
#     if score % 5 == 0 and score != 0:
#         screen.blit(monster, monster_pos)    
        
    #collision on body
    for i in range(len(snake) - 1, 0, -1):
        if collisionBody(snake[0], snake[i]):
            game = False
            
#     #collision on monster    
#     if collisionMonster(snake[0], monster_pos):
#         game = False
    
    #collision on border
    if collisionBorder(snake[0]):
        game = False
        
    #make snake walk
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
    
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
        
    pygame.display.update()
