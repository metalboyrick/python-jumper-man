import pygame, sys

# initialisation
pygame.init()
clock = pygame.time.Clock()

# Screen initialisation
screen_width = 700
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jumper Man")

# Game loop
while True:

    # Handle input
    for event in pygame.event.get():

        # Handle quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # window update
    pygame.display.flip()
    clock.tick(60)




