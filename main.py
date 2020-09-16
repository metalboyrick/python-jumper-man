import pygame, sys
from floor import Floor

# initialisation
pygame.init()
clock = pygame.time.Clock()

# Screen initialisation
screen_width = 700
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jumper Man")

# import assets
# background
bg_surface = pygame.image.load('assets/bg.png').convert()   # converting to PyGame-friendly

# floor
floor = Floor(image_path='assets/tile.png',width=497,height=99)
floor.scale_twice()

# Game loop
while True:

    # this is the event loop
    for event in pygame.event.get():

        # Handle quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    

    # draws background on surface
    screen.blit(bg_surface,(0,0))

    # floor movement
    floor.draw_to_screen(screen_obj=screen,\
                        vertical_pos=200,\
                        screen_width=screen_width,\
                        speed=6)


    # window update
    pygame.display.update()
    clock.tick(60)




