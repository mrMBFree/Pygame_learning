import pygame ,math
import spritesheet


PLAYER_START_X = 400
PLAYER_START_Y = 500
PLAYER_SPEED = 5

class Player(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.pos = pygame.math.Vector2(PLAYER_START_X,PLAYER_START_Y)
        self.speed = PLAYER_SPEED

    def user_input(self):
        self.velocity_x = 0
        self.velocity_y = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.velocity_y = -self.speed
        if keys[pygame.K_s]:
            self.velocity_y = self.speed
        if keys[pygame.K_d]:
            self.velocity_x = self.speed
        if keys[pygame.K_a]:
            self.velocity_x = -self.speed    

        if self.velocity_x !=0 and self.velocity_y !=0: #poruszanie sie na skos
            self.velocity_x /= math.sqrt(2)
            self.velocity_y /= math.sqrt(2)
    def move(self):
        self.pos += pygame.math.Vector2(self.velocity_x, self.velocity_y) 

    def update(self):
        self.user_input()
        self.move()

pygame.init() #zaczynamy z pygame 
clock = pygame.time.Clock()
FPS = 60 

screen = pygame.display.set_mode((1200,600))

sprite_sheet_image = Player('./moving_animations/links.gif')
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image.image)

BG = (50, 50, 50)
BLACK = (0, 0, 0)

#create animation list
animation_list = []
animation_steps = [1,7,1,7,1,7,1,7] #[prawo, dol,lewo ,gora]

action = 0

last_update = pygame.time.get_ticks()
animation_cd = 75

frame = 0

step_counter = 0

for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, 100, 100, 1, BLACK))
        step_counter += 1
    animation_list.append(temp_img_list)

direction = "right"

run = True
while run:

    clock.tick(FPS)
    screen.fill(BG)

    #update animation only if the character is moving

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cd:
        frame +=1 
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0

    #SHOW FRAME IMAGE
    screen.blit(animation_list[action][frame], sprite_sheet_image.pos)
    sprite_sheet_image.update()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
            
         # Check for movement keys and set the action and frame accordingly
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                action = 7
                frame = 0
            if event.key == pygame.K_s:
                action = 3
                frame = 0
            if event.key == pygame.K_d:
                action = 1
                frame = 0
            if event.key == pygame.K_a:
                action = 5
                frame =0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                action = 6
                frame = 0
            if event.key == pygame.K_s:
                action = 2
                frame = 0
            if event.key == pygame.K_d:
                action = 0
                frame = 0
            if event.key == pygame.K_a:
                action = 4
                frame = 0
         # Reset the is_moving flag before checking the movement keys



    pygame.display.update()
pygame.quit()