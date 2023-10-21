

import pygame

# create a window object
DISPLAY = [1280, 720]
BACKGROUND = [255, 255, 255]
FPS = 60

window = pygame.display.set_mode(DISPLAY)
clock = pygame.time.Clock()


# ------------------------------

block = pygame.image.load('red.png')

# ------------------------------


running = True
while running:
    # pause the game for a certain amount of time
    clock.tick(FPS)

    # handle events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        
        elif e.type == pygame.KEYDOWN:
            pass
        elif e.type == pygame.KEYUP:
            pass
    
    # update the game


    # draw everything
    window.fill(BACKGROUND)
    window.blit(block, (100, 100))


    # update the window
    pygame.display.update()

# ------------------------------
pygame.quit()






