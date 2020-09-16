import pygame

# draw floors easily
class Floor():
    # constructor for floor class
    def __init__(self, image_path, width, height):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.width = width
        self.height = height
        self.x_pos = 0
        self.y_pos = 0

    # scale twice
    def scale_twice(self):
        self.image = pygame.transform.scale2x(self.image)
        self.width = 2 * self.width
        self.height = 2 * self.height


    # this will draw a scrolling floor
    def draw_to_screen(self, screen_obj,vertical_pos, screen_width, speed):  
        self.x_pos -= speed
        screen_obj.blit(self.image,(self.x_pos, vertical_pos))
        screen_obj.blit(self.image,(screen_width + self.x_pos, vertical_pos))

        if self.x_pos < screen_width * -1:
            self.x_pos = 0
