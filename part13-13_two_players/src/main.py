# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window_width,window_height = 640,480

window = pygame.display.set_mode((window_width, window_height))

robot1 = pygame.image.load("robot.png")
robot2 = pygame.image.load("robot.png")

robot_width,robot_height = robot1.get_width(),robot1.get_height()

x1,y1 = 100,150
x2,y2 = 300,250

to_left1 = to_right1 = to_up1 = to_down1 = False
to_left2 = to_right2 = to_up2 = to_down2 = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left1 = True
            if event.key == pygame.K_RIGHT:
                to_right1 = True
            if event.key == pygame.K_UP:
                to_up1 = True
            if event.key == pygame.K_DOWN:
                to_down1 = True

            if event.key == pygame.K_a:
                to_left2 = True
            if event.key == pygame.K_d:
                to_right2 = True
            if event.key == pygame.K_w:
                to_up2 = True
            if event.key == pygame.K_s:
                to_down2 = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left1 = False
            if event.key == pygame.K_RIGHT:
                to_right1 = False
            if event.key == pygame.K_UP:
                to_up1 = False
            if event.key == pygame.K_DOWN:
                to_down1 = False
            
            if event.key == pygame.K_a:
                to_left2 = False
            if event.key == pygame.K_d:
                to_right2 = False
            if event.key == pygame.K_w:
                to_up2 = False
            if event.key == pygame.K_s:
                to_down2 = False
            
            

    if to_right1 and (x1+robot_width <= window_width):
        x1 += 2
    if to_left1 and (x1 >=0):
        x1 -= 2
    if to_up1 and y1 >=0:
        y1 -= 2
    if to_down1 and (y1+robot_height <= window_height):
        y1 += 2
    
    if to_right2 and (x2+robot_width <= window_width):
        x2 += 2
    if to_left2 and (x2 >=0):
        x2 -= 2
    if to_up2 and y2 >=0:
        y2 -= 2
    if to_down2 and (y2+robot_height <= window_height):
        y2 += 2
    
    window.fill((0,0,0))
    window.blit(robot1,(x1,y1))
    window.blit(robot2,(x2,y2))
    pygame.display.flip()

    clock.tick(60)