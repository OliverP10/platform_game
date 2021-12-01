import pygame
from backgroundmap import MotionPlatform
from spritecollection import SpriteCollection
import time


class Player():

    def __init__(self):
        self.moving_left = False
        self.moving_right = False
        self.change_x = 0
        self.change_y = 0

        sprite_sheet = SpriteCollection("textures/stickman.png")
        self.image = sprite_sheet.get_image(0, 0, 20, 20)
        self.image.set_colorkey((255,255,255))
        self.collision_box = self.image.get_rect()
        
        self.airbourne = False

    def draw_player(self,surface,scroll):
        surface.blit(self.image, (self.collision_box.x-scroll[0],self.collision_box.y))

    def test_collisions(self,objects):
        collisions = []
        for object in objects:
            if self.collision_box.colliderect(object.collision_box):
                collisions.append(object)
        return collisions

    def update(self, objects):
        if self.moving_right == False and self.moving_left == False:
            self.change_x = 0
        if self.moving_left:
            self.change_x = -2
        if self.moving_right:
            self.change_x = 2
        
        if self.change_y < 6:
            self.change_y += 0.3
               
        collision_direction = [False,False,False,False] #format for collions: LEFT,RIGH,UP,DOWN

        
        self.collision_box.x += self.change_x
        
        collisions = self.test_collisions(objects)
        for collision in collisions:
            if self.change_x < 0:   #If colliding left
                self.collision_box.left = collision.collision_box.right
                collision_direction[0] = True
            if self.change_x > 0:   #If colliding right
                self.collision_box.right = collision.collision_box.left
                self.collision_box
                collision_direction[1] = True

        self.collision_box.y += self.change_y

        collisions = self.test_collisions(objects)
        for collision in collisions:
            if self.change_y > 0:   #If colliding bottom
                self.collision_box.bottom = collision.collision_box.top
                collision_direction[3] = True
                
                
            if self.change_y < 0:   #If colliding top
                self.collision_box.top = collision.collision_box.bottom
                collision_direction[2] = True            

        if not collision_direction[3]:  #If not colliding bottom
            self.airbourne = True
        else:
            self.airbourne = False


    def jump(self):
        if not self.airbourne:
            self.change_y -= 15

