import pygame
from animation import Animation

class Player():

    def __init__(self):
        self.moving_left = False
        self.moving_right = False
        self.change_x = 0
        self.change_y = 0

        self.animation_right = Animation("textures/stickman_animation_sheet.png", False, 0.1)
        self.animation_left = Animation("textures/stickman_animation_sheet.png", True, 0.1)
        
        self.image = self.animation_right.get_image()
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

        if self.change_y < 6:   #termianl velocity
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
                collision_direction[1] = True

        self.collision_box.y += self.change_y

        collisions = self.test_collisions(objects)
        for collision in collisions:
            if self.change_y > 0:   #If colliding bottom
                self.collision_box.bottom = collision.collision_box.top
                collision_direction[3] = True
                #need to move the jump into here so the update orders work correctly
                
            if self.change_y < 0:   #If colliding top
                self.collision_box.top = collision.collision_box.bottom
                collision_direction[2] = True
                self.change_y = 0

        if not collision_direction[3]:  #If not colliding bottom
            self.airbourne = True
        else:
            self.airbourne = False


    def jump(self):
        if not self.airbourne:
            self.change_y -= 15


    

