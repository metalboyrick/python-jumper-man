import pygame, sys

# pygame initialisation
pygame.init()
clock = pygame.time.Clock()

# game settings
GRAVITY = 0.5
MOVEMENT_SPEED = 3
JUMP_FORCE = 10
PR_ENEMY = 0
RUN_MOTION_SPEED = 100

# Screen initialisation
screen_width = 497
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jumper Man")

### background
bg_surface = pygame.image.load('assets/bg.png').convert()   # converting to PyGame-friendly

### floor
floor_surface = pygame.image.load('assets/tile.png')
floor_rect1 = floor_surface.get_rect(center=(248,250))
floor_rect2 = floor_surface.get_rect(center=(745,250))
floor_x_pos = 0

### character
# surfaces and rects
hero_run_frames = [pygame.transform.scale2x(pygame.image.load(
    'assets/adventurer-run-0' + str(i) + '.png').convert_alpha()) for i in range(0, 6)]
hero_jump = pygame.image.load('assets/adventurer-jump-03.png')
hero_jump = pygame.transform.scale2x(hero_jump)
hero_rect = hero_jump.get_rect(center=(100, 167))
hero_surface = hero_jump                                                                    # this variable points to the current hero sprite used

# hero-related variables
hero_y_offset = 0       # difference from original to current position
is_jumping = False      # jump flag
run_index = 0           # index that points to current frame of running motion

# custom events
E_HERO_RUN = pygame.USEREVENT                           # event taht fires with regular intervals
pygame.time.set_timer(E_HERO_RUN, RUN_MOTION_SPEED)     # set the even interval


# Game loop
while True:

    # this is the event loop
    for event in pygame.event.get():

        # Handle quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle Keypress
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                # decrement by jump force to lift character up
                hero_y_offset -= JUMP_FORCE

                # set flag to true, prevents combo jumping
                is_jumping = True

        # Handle Running animation
        if event.type == E_HERO_RUN:
            
            if not is_jumping:
                # index cyclic increments
                run_index += 1  
                run_index = run_index % 6

                # animation for hero
                hero_surface = hero_run_frames[run_index]
            else:
                # character is jumping
                hero_surface = hero_jump
    
        
    ### draws background on surface
    screen.blit(bg_surface,(0,0))

    ### draw floor + movement
    floor_x_pos -= MOVEMENT_SPEED

    # positioning of the two floor tiles
    floor_rect1.centerx = floor_x_pos + 248
    floor_rect2.centerx = floor_x_pos + 745

    # draw them
    screen.blit(floor_surface, floor_rect1)
    screen.blit(floor_surface, floor_rect2)

    # tile resetting
    if floor_x_pos < -497:
        floor_x_pos = 0

    ### Hero drawing
    # get offset and draw rectangle
    hero_rect.centery += hero_y_offset
    hero_rect = hero_surface.get_rect(center=(100, hero_rect.centery))
    
    # draw character on screen
    screen.blit(hero_surface, hero_rect)

    # gravity logic
    if hero_rect.colliderect(floor_rect1) or hero_rect.colliderect(floor_rect2):
        hero_y_offset = 0
        is_jumping = False
    else:
        hero_y_offset += GRAVITY
    

    # window update
    pygame.display.flip()
    clock.tick(120)
