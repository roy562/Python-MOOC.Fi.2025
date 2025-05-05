# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()

window_width,window_height  = 640,480

window = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Asteroids")

robot = pygame.image.load("robot.png")
rock  = pygame.image.load("rock.png")

robot_width, robot_height = robot.get_width(), robot.get_height()
rock_width, rock_height = rock.get_width(), rock.get_height()

robot_x = window_width/2-robot_height/2
robot_y = window_height - robot_height

game_font = pygame.font.SysFont("Arial", 24)

rocks = []

to_left = False
to_right = False

points = 0

game_finished = False

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
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False

    window.fill((0,0,0))

    if not game_finished:
        if to_right and (robot_x+robot_width <= window_width):
            robot_x += 3
        if to_left and (robot_x >=0):
            robot_x -= 3

        if random.randint(1, 100) == 1:
            rock_x = random.randint(0,640-rock_width)
            rock_y = - rock_height
            rocks.append([rock_x, rock_y])
        
        for r in rocks:
            r[1] += 1

            robot_dims = robot.get_rect(topleft=(robot_x, robot_y))
            rock_dims = rock.get_rect(topleft=(r[0], r[1]))

            if robot_dims.colliderect(rock_dims):
                rocks.remove(r)
                points += 1
            elif r[1] >= 480 - rock_height:
                game_finished = True

            window.blit(rock, (r[0], r[1]))
        
        window.blit(robot, (robot_x, robot_y))
        text = game_font.render(f"Points: {points}", True, (255, 0, 0))
        window.blit(text, (550, 10))

    else:
        text = game_font.render(f"Points: 0", True, (255, 0, 0))
        window.blit(robot, (0, window_height - robot_height))
        window.blit(text, (550, 10))
    
    pygame.display.flip()
    clock.tick(60)