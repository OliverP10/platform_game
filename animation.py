import pygame
from spritecollection import SpriteCollection

class Animation():

    def __init__(self, file_name,flip_image,animation_speed):
        sprite_sheet = SpriteCollection(file_name)
        self.images = sprite_sheet.get_all_image(20, 20,flip_image)
        self.image_pointer = 0
        self.animation_speed=animation_speed
        

    def get_image(self):
        return self.images[int(self.image_pointer)]

    def tick(self):
        self.image_pointer+=self.animation_speed
        if self.image_pointer > len(self.images):
            self.image_pointer = 0

