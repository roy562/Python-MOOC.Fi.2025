# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
window.fill((0,0,0))

width = robot.get_width()
height = robot.get_height()

start_x = 50
start_y = 70

for i in range(0,10):
    for j in range(0,10):
        window.blit(robot, (start_x+j*40, start_y))
    start_y+=20
    start_x+=10

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()