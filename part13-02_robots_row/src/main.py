# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
window.fill((0,0,0))

width = robot.get_width()
height = robot.get_height()

no_of_robots = 10

start_x = 50
start_y = 100

for i in range(0,10):
    window.blit(robot, (start_x+i*width, start_y))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()