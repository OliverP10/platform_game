import pygame
from spritecollection import SpriteCollection

GRASS_LEFT = (576, 720, 70, 70)
GRASS_RIGHT = (576, 576, 70, 70)
GRASS_MIDDLE = (504, 576, 70, 70)
STONE_PLATFORM_LEFT = (432, 720, 70, 40)
STONE_PLATFORM_MIDDLE = (648, 648, 70, 40)
STONE_PLATFORM_RIGHT = (792, 648, 70, 40)


class Platform(pygame.sprite.Sprite):

    def __int__(self, sprite_data):
        super().__init__()

        sprite_sheet = SpriteCollection("textures/tiles_spritesheet.png")

        self.image = sprite_sheet.get_image(sprite_data[0], sprite_data[1], sprite_data[2], sprite_data[3])
        self.rect = self.image.get_rect()


class MotionPlatform(Platform):

    def __init__(self, sprite_data):

        super().__init__(sprite_data)

        self.change_x = 0
        self.change_y = 0
        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0
        self.level = None
        self.player = None

    def update(self):

        self.rect.y += self.change_y
        hit = pygame.sprite.collide_rect(self, self.player)

        if hit:
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        currentpos = self.rect.x - self.level.world_shift
        if currentpos < self.boundary_left or currentpos > self.boundary_right:
            self.change_x *= -1
