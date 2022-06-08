import pygame, sys
from pygame.locals import *
 
FPS = 50
silver = (194, 194, 194)
black = (0, 0, 0)
 
pygame.init()
screen = pygame.display.set_mode((600, 400),RESIZABLE, 32)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Ubuntu Condensed", 35, bold=False, italic=False)
year = 2021
 
while True:
    clock.tick(FPS)
    for i in pygame.event.get():
        if i.type == QUIT:
            pygame.quit()
            sys.exit()
        elif i.type == KEYDOWN:
            print(i.key)
    year = year + 1
    screen.fill(black)
    text = font.render("Hello world! "+str(year)+" year!",True,silver)
    screen.blit(text, [150,170])
    pygame.display.update()