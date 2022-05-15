import pygame
import math
from itertools import repeat
pygame.init()


# CLASSES
class Outer_Circle():
    @staticmethod
    def draw():
        pygame.draw.circle(screen, center=(WIDTH/2, HEIGHT/2), radius=outer_radius, width=2, color=main_color)

class Inner_Circle():
    def __init__(self):
        self.arg = 0
        self.radius = outer_radius * ratio
    
    def draw(self, add:bool):
        center = tuple(map(lambda x, y, z: x + y*z, (WIDTH/2, HEIGHT/2), (math.cos(-self.arg), math.sin(-self.arg)), repeat(outer_radius-self.radius)))
        dot = tuple(map(lambda x, y, z: x + y*z, center, (math.cos(self.arg/speed_boost), math.sin(self.arg/speed_boost)), repeat(self.radius)))
        pygame.draw.circle(
            screen,
            center = center,
            radius = self.radius,
            width = 2,
            color = main_color
        )
        pygame.draw.circle(
            screen,
            center = center,
            radius = 3,
            color = main_color
        )
        pygame.draw.line(
            screen,
            start_pos = center,
            end_pos = dot,
            color = main_color
        )
        if add:
            dots.append(dot)
    
    def move(self):
        self.arg += 0.01


# INITIALIZING VARIABLES
FPS = 60
frame_counter = 0
outer_radius = 360
main_color = (160, 8, 210) #a008d2
accent_color = (255, 119, 0) #ff7700
add_flag = True

ratio = tuple(map(float, input("\nInput circles' radius ratio. Example: 1/3\n>> ").split("/")))
if ratio[0] > ratio[1]:
    raise ValueError("Man, no, that won't work")
ratio, speed_boost, stop_adding_frame = ratio[0] / ratio[1], ratio[0] / (ratio[1] - ratio[0]), ratio[0] * 630

inner_circle = Inner_Circle()
dots = []

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Say "Hello" to hypocycloid!')
clock = pygame.time.Clock()


# MAINLOOP
done = False
while not done:
    clock.tick(FPS)
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    Outer_Circle.draw()
    inner_circle.draw(add_flag)
    for dot in dots:
        pygame.draw.circle(
            surface = screen,
            center = dot,
            radius = 4,
            color = accent_color
        )
    
    inner_circle.move()
    
    pygame.display.flip()
    frame_counter += 1
    if frame_counter == stop_adding_frame: # avoiding MemoryError when too many dors are here
        add_flag = False
    if frame_counter == FPS*1000: # for not to keep too large numbers
        frame_counter = 0