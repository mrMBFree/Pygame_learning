import pygame,random

class Cross(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.gunshoot = pygame.mixer.Sound('./sprites/ui_goku.mp3')
        self.playing_sound = False
    def shoot(self):
        if not self.playing_sound:  # Sprawdzamy, czy dźwięk nie jest już odtwarzany
            self.gunshoot.play()
            self.playing_sound = True
        pygame.sprite.spritecollide(cross,target_group,True)
    def update(self):
        self.rect.center = pygame.mouse.get_pos()   

class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, posx,posy):
        super().__init__()
        self.image = pygame.image.load(picture_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [posx,posy]


pygame.init()
clock = pygame.time.Clock()
FPS = 60 


screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('sprites')
bg = pygame.image.load('./sprites/bg_blue.png').convert()
bg_update = pygame.transform.scale(bg, (1200,600))

pygame.mouse.set_visible(False)

#cross 
cross = Cross('./sprites/crosshair_red_large.png')
cross_group = pygame.sprite.Group()
cross_group.add(cross)

#target
target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target('./sprites/target_red1.png', random.randrange(0,screen.get_width()),random.randrange(0,screen.get_height()))
    target_group.add(new_target)


run = True
while run:

    for event in pygame.event.get():
         if event.type == pygame.QUIT:
              run = False
         if event.type == pygame.MOUSEBUTTONDOWN:
             cross.shoot()

    pygame.display.flip()
    clock.tick(FPS)
    screen.blit(bg_update, (0,0))
    cross_group.draw(screen)
    cross_group.update()
    target_group.draw(screen)
    if not pygame.mixer.get_busy():  # Sprawdzamy, czy dźwięk przestał się odtwarzać
        cross.playing_sound = False
pygame.quit()





