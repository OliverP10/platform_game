import pygame
from pygame.locals import * # import pygame modules
from textures import Texture
from items import Item

class Platform():

    def __init__(self):
        self.background_objects = []
        self.background_items = []

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
                self.background_items.append(item)


    def draw_background(self,surface, scroll):
        for object in self.background_objects:
            surface.blit(object.image, (object.collision_box.x-scroll[0],object.collision_box.y))
        for object in self.background_items:
            surface.blit(object.image, (object.rect.x-scroll[0],object.rect.y))
            object.animation_tick()

class Background_object():

    def __init__(self,x,y,textue_image):
        self.image = textue_image
        self.collision_box = pygame.Rect(x,y,self.image.get_width(),self.image.get_height())




        
        