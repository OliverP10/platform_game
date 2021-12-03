import pygame
from background import Platform
from player import Player

clock = pygame.time.Clock()
pygame.init() # initiates pygame
pygame.display.set_caption('Pygame Platformer')
WINDOW_SIZE = (1200,900)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window
display = pygame.Surface((600,400)) # used as the surface for rendering, which is scaled

scroll = [0,0]
platform = Platform()
platform.load_objects("maps/map1.txt")

player = Player()


sprites = pygame.sprite.Group()
sprites.add

while True: # game loop
    display.fill((136,234,245)) # clear screen by filling it with blue

    scroll[0]+= (player.collision_box.x-scroll[0]-310)/20

    platform.draw_background(display,scroll)
    player.update(platform.background_objects)
    player.draw_player(display,scroll)

    for event in pygame.event.get(): # event loop
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.moving_left=True
            if event.key == pygame.K_RIGHT:
                player.moving_right=True
            if event.key == pygame.K_UP:
                player.jump=True
                
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            if event.key == pygame.K_LEFT:
                player.moving_left = False
                
    
    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    pygame.display.update()
    clock.tick(60)


#Thigs to do
#Make the items and backgorund objects load images in the same way!