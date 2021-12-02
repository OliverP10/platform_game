import pygame

class SpriteCollection(object):

    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return image

    def get_all_image(self, width, height, flip):
        #x_count = int(self.sprite_sheet.get_width()/width)
        #y_count = int(self.sprite_sheet.get_height()/height)
        #print(x_count)
        #print(y_count)
        images = []
 
        for y in range(0,self.sprite_sheet.get_height(),height):
            for x in range(0,self.sprite_sheet.get_width(),width):
                image = pygame.Surface([width, height]).convert()
                image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
                image.set_colorkey((255,255,255))
                if flip:
                    image = pygame.transform.flip(image, True, False)
                images.append(image)

        
        return images

    #overload this method and do one where it takes an optional paremtre list of
    # stings and then use a dictionry to apply the name tags to the images