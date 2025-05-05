# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")

x = 320
y = 240

width = ball.get_width()
height = ball.get_height()

velocity_x = 2
velocity_y = 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()

    if x <= 0 or x+width >= 640:
        velocity_x = -velocity_x
    if y <= 0 or y+height >= 480:
        velocity_y = -velocity_y

    x+=velocity_x
    y+=velocity_y

    clock.tick(60)