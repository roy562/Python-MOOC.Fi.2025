# WRITE YOUR SOLUTION HERE:
import pygame
import random 

pygame.init()

window_width, window_height = 640, 480
window = pygame.display.set_mode((window_width, window_height))

robot = pygame.image.load("robot.png")

robot_width, robot_height = robot.get_width(), robot.get_height()

x = random.randint(0,window_width-robot_width)
y = random.randint(0,window_height-robot_height)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        mouse_x, mouse_y = 0,0

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

        hit_x = mouse_x >= x and mouse_x <= x+robot_width
        hit_y = mouse_y >= y and mouse_y <= y+robot_height

        if hit_x and hit_y:
            x = random.randint(0,window_width-robot_width)
            y = random.randint(0,window_height-robot_height)

    window.fill((0, 0, 0))
    window.blit(robot, (x,y))
    pygame.display.flip()

    clock.tick(60)