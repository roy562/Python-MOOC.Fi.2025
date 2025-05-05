# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window_width = 640
window_height = 480

window = pygame.display.set_mode((window_width, window_height))

robot = pygame.image.load("robot.png")

robot_width = robot.get_width()
robot_height = robot.get_height()

x = window_width/2-robot_width/2
y = window_height/2-robot_height/2

to_left = False
to_right = False
to_up = False
to_down = False

velocity = 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False

    if to_right and (x+robot_width <= window_width):
        x += 2
    if to_left and (x >=0):
        x -= 2
    if to_up and y >=0:
        y -= 2
    if to_down and (y+robot_height <= window_height):
        y += 2
    
    window.fill((0,0,0))
    window.blit(robot,(x,y))
    pygame.display.flip()

    clock.tick(60)