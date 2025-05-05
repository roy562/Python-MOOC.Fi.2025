# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

robots = []
for i in range(20):
    initial_x = random.randint(0,640-width)
    initial_y = -random.randint(100,1000)
    x_direction = random.choice([-1,1])
    robots.append([initial_x, initial_y, x_direction])

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    for i in range(20):
        if robots[i][1]+height < 480:
            robots[i][1]+=1
        else:
           robots[i][0]+=robots[i][2]
        window.blit(robot, (robots[i][0], robots[i][1]))

    pygame.display.flip()
    
    
    clock.tick(60)