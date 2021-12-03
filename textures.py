import pygame
from spritecollection import SpriteCollection

class Texture():

    def __init__(self):
        self.images = {}

    def load_all(self):
        sprite_sheet = SpriteCollection("textures/background_tiles.png")
        textures = sprite_sheet.get_all_image(20, 20,False)
        with open("textures/index.txt") as f:
            texture_names = f.read().split("\n")
        for i in range(len(textures)):
            self.images[texture_names[i]] = textures[i]


    def load_grass_bloc(self):
        #sprite_sheet = SpriteCollection("textures/tiles_spritesheet.png")
        #image = sprite_sheet.get_image(0, 0, 66, 90)
        image = pygame.image.load("textures/dirt.png").convert()
        self.images["grass_bloc"] = image

    

