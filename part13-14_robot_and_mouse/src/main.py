# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

clock = pygame.time.Clock()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            window.fill((0, 0, 0))
            window.blit(robot, (event.pos[0]-robot.get_width()/2, event.pos[1]-robot.get_height()/2))
            pygame.display.flip()

        if event.type == pygame.QUIT:
            exit(0)
    

    clock.tick(60)