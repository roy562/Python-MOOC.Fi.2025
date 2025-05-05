# WRITE YOUR SOLUTION HERE:
import pygame
import datetime
import math

pygame.init()

window_width, window_height = 640, 480
center = (window_width/2, window_height/2)
clock_radius = 180

color_black = (0,0,0)
color_red = (255,0,0)
color_blue = (0,0,255)

window = pygame.display.set_mode((window_width, window_height))


def draw_circles():
    pygame.draw.circle(window, color_red, center, clock_radius, 2)
    pygame.draw.circle(window, color_red, center, 10)

def get_angles():
    curr_time = datetime.datetime.now()
    seconds = (curr_time.second*6)-90
    minutes = (curr_time.minute*6 + curr_time.second*0.1)-90
    hours = ((curr_time.hour % 12) * 30) + (curr_time.minute * 0.5) - 90
    return hours, minutes, seconds

def get_line_coord(angle, radius):
        x = center[0]+math.cos(math.radians(angle))*radius
        y = center[1]+math.sin(math.radians(angle))*radius
        return x,y

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill(color_black)
    draw_circles()

    angle_hour, angle_minute, angle_second = get_angles()

    #Set screen to reflect current time
    pygame.display.set_caption(datetime.datetime.now().strftime("%H:%M:%S"))

    #draw seconds, minutes and hours lines
    pygame.draw.line(window, color_blue, center, get_line_coord(angle_second, clock_radius*0.9), 1)
    pygame.draw.line(window, color_blue, center, get_line_coord(angle_minute, clock_radius*0.8), 2)
    pygame.draw.line(window, color_blue, center, get_line_coord(angle_hour, clock_radius*0.5), 4)
    pygame.display.flip()

    clock.tick(60)