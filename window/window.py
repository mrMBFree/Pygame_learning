import pygame  #biblioteka pygame
import os  #bibliotke os


pygame.init() #zaczynamy z pygame 
clock = pygame.time.Clock()
FPS = 60 

os.environ['SDL_VIDEO_CENTERED'] = '1' #called before pygame.init()
info = pygame.display.Info() #called before set_mode
screen_width, screen_height = info.current_w , info.current_h

'''screen = pygame.display.set_mode((1200,600))''' # okienko 500 na 300 px

screen = pygame.display.set_mode((screen_width -10,screen_height -50), pygame.RESIZABLE) #MOZEMY DZIEKU TEMU POWIEKSZYC OKNO DO MAKS ROZMIARU (TO NIE JEST FULLSCREN)
                                                #.FULLSCREEN , to nam da Fullscreen
run = True
while run:

    clock.tick(FPS)

    for event in pygame.event.get():
         if event.type == pygame.QUIT:
              run = False

    pygame.display.update()
pygame.quit()
# cała sekwencja tworzy petla ktora dziala dopoki uzytkownik nie zamknie okna

