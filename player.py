import pygame
from animation import Animation
import math

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.moving_left = False
        self.moving_right = False
        self.jump = False
        self.change_x = 0
        self.change_y = 0

        self.animation_right = Animation("textures/stickman_animation_sheet.png", False, 0.1)
        self.animation_left = Animation("textures/stickman_animation_sheet.png", True, 0.1)
        
        self.image = self.animation_right.get_image()
        self.rect = self.image.get_rect()

        self.airborne = False

    def draw_player(self,surface,scroll):
        surface.blit(self.image, (self.rect.x - scroll[0], self.rect.y))

    def test_collisions(self,objects):
        collisions = []
        for object in objects:
            if self.rect.colliderect(object.rect):
                collisions.append(object)
        return collisions

    def update(self, objects):
        self.animation_left.tick()
        self.animation_right.tick()

        if self.moving_right == False and self.moving_left == False:
            self.change_x = 0
        if self.moving_left:
            self.change_x = -2
            self.animation_right.image_pointer=0
            self.image = self.animation_left.get_image()
        if self.moving_right:
            self.change_x = 2
            self.animation_left.image_pointer=0
            self.image = self.animation_right.get_image()
        if self.jump:
            if not self.airborne:
                self.change_y -= 6
            self.jump=False
        
        if self.change_y < 6:   #termianl velocity
                self.change_y += 0.3

        collision_direction = [False,False,False,False] #format for collions: LEFT,RIGH,UP,DOWN
        self.rect.x += self.change_x
        
        collisions = self.test_collisions(objects)
        for collision in collisions:
            if self.change_x < 0:   #If colliding left
                self.rect.left = collision.rect.right
                collision_direction[0] = True
            if self.change_x > 0:   #If colliding right
                self.rect.right = collision.rect.left
                collision_direction[1] = True

        self.rect.y += math.ceil(self.change_y)    #Will brake the collions is this is int for some reason

        collisions = self.test_collisions(objects)
        for collision in collisions:
            if self.change_y >= 0:   #If colliding bottom
                
                self.rect.bottom = collision.rect.top
                collision_direction[3] = True
                
                
            if self.change_y < 0:   #If colliding top
                self.rect.top = collision.rect.bottom
                collision_direction[2] = True

        
        
        if not collision_direction[3]:  #If not colliding bottom
            self.airborne = True
        else:
            self.airborne = False
            self.change_y = 0


        


    

