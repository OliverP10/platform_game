import pygame
from animation import Animation

class Item(pygame.sprite.Sprite):

    def __init__(self,x, y, image_fn):
        super().__init__()
        self.animaition = Animation("textures/"+image_fn+".png", False, 0.1)
        self.image = self.animaition.get_image()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #Add cutstom collsion box
        #make it so imag animates

    def pick_up(self):  #FIX
        self.animaition = Animation("textures/sword_power_up_held.png", False, 0.1)
        self.image = self.animaition.get_image()
        self.rect = self.image.get_rect()

    def animation_tick(self):
        self.animaition.tick()

    