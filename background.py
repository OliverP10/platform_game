import pygame
from pygame.locals import * # import pygame modules

from textures import Texture
from items import Item

class Platform():

    def __init__(self):
        self.background_objects = []
        self.item_group = None

    # getter, setter and deleter decorator for attribute
    @property
    def item_group(self):
        return self._item_group

    @item_group.setter
    def item_group(self, value):
        self._item_group = value

    @item_group.deleter
    def item_group(self):
        del self._item_group

    def load_objects(self, file_name):  #Takes file name and adds Background_objects to a attribute list
        texture = Texture()
        texture.load_all()
        lines = []
        with open(file_name) as f:
            lines = f.readlines()
        for line in lines:
            data = line.split(',')  #splits each line of text file into a list format - X,Y,IMAGE,TYPE,NUMBER OF REAPEATS
            if data[3] == "block":
                offset = 0
                for i in range(int(data[4])):
                    image = texture.images[data[2]]
                    bg_object = Background_object(int(data[0])+offset,int(data[1]),image)
                    offset += image.get_width()
                    self.background_objects.append(bg_object)
            elif data[3] == "item":
                item = Item(int(data[0]),int(data[1]),data[2])
                self.item_group.add(item)


    def draw_background(self,surface, scroll):
        for object in self.background_objects:
            surface.blit(object.image, (object.rect.x - scroll[0], object.rect.y))
        for object in self.item_group:
            surface.blit(object.image, (object.rect.x-scroll[0],object.rect.y))
            object.animation_tick()

class Background_object():

    def __init__(self, x, y, texture_image):
        self.image = texture_image
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

class Game_values():

    def __init__(self):
        self.environment = {
            "gravity": 0.3,
            "air_resistance": 1
        }
        self.player = {
            "speed": 2,
            "jump": 6,
            "airbourne_movment": 0.001
        }





        
        