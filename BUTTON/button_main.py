import pygame
import button #bierzemy z pliku button.py

pygame.init()

screen = pygame.display.set_mode((700,500))
pygame.display.set_caption('BUtton demo') #tytul okienka

#importujemy zdjecia
start_img = pygame.image.load('./BUTTON/start_btn.png').convert_alpha() #convertalpha gives better performance 
exit_img = pygame.image.load('./BUTTON/exit_btn.png').convert_alpha()


#button instansces
start_button = button.Button(100,200, start_img, 0.5)
exit_button = button.Button(450,200, exit_img, 0.5)

run = True
while run:
    screen.fill((202,228,241)) #dajemy tło
    #start_button.draw() #wstawiamy obraz do okna
    #exit_button.draw()

    if start_button.draw(screen):
        print('star')
    if exit_button.draw(screen):
        #print('exit')    
        run = False

    for event in pygame.event.get():
         if event.type == pygame.QUIT:
              run = False

    pygame.display.update()
pygame.quit()