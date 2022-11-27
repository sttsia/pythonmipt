import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
polygon(screen, (120, 120, 120), [(0, 0), (0, 400), (400, 400), (400, 0)])
#лицо
circle(screen, (255, 255, 0), (200, 200), 100)
#обводка смайла
circle(screen, (255, 255, 255), (200, 200), 100, 1)
#глаза
circle(screen, (255, 0, 0), (155, 190), 20)
circle(screen, (255, 0, 0), (250, 190), 15)
#обводка глаз
circle(screen, (0, 0, 0), (155, 190), 20, 1)
circle(screen, (0, 0, 0), (250, 190), 15, 1)
#зрачки
circle(screen, (0, 0, 0), (155, 190), 5)
circle(screen, (0, 0, 0), (250, 190), 5)
#брови
polygon(screen, (0, 0, 0), [(100, 100), (180, 165), (185, 175), (95, 105)])
polygon(screen, (0, 0, 0), [(215, 175), (213, 167), (300, 125), (305, 130)])
polygon(screen, (0, 0, 0), [(130, 260), (270, 260), (270, 250), (130, 250)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
