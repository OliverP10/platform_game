import pygame
from spritecollection import SpriteCollection

class Texture():

    def __init__(self):
        self.images = {}

    def load_all(self):
        pass

    def load_grass_bloc(self):
        sprite_sheet = SpriteCollection("textures/tiles_spritesheet.png")
        image = sprite_sheet.get_image(0, 0, 66, 90)
        image = pygame.image.load("textures/dirt.png").convert()
        self.images["grass_bloc"] = image

    

