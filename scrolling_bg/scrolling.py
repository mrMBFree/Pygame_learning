import pygame
import math

pygame.init()

#USTAWIAMY STALA LICZBE FPS
clock = pygame.time.Clock()
FPS = 60 

screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('scroling')

bg = pygame.image.load('./scrolling_bg/bg.png').convert()
bg_width = bg.get_width()

scroll = 0
tiles = math.ceil(screen.get_width()/bg_width ) +1

run = True
while run:

    clock.tick(FPS)

    #tło
    for i in range(0, tiles):
         screen.blit(bg,(i*bg_width + scroll,0))

    #scrooll bg
    scroll -= 1

    #reset scroll
    if abs(scroll) > bg_width:
        scroll = 0

    for event in pygame.event.get():
         if event.type == pygame.QUIT:
              run = False

    pygame.display.update()
pygame.quit()
