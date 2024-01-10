import pygame
import time

# import the new classes

from scripts import entity
from scripts import handler
from scripts import inputhandler


# create a window object
DISPLAY = [1280, 720]
BACKGROUND = [0, 255, 255]
FPS = 60

window = pygame.display.set_mode(DISPLAY)
clock = pygame.time.Clock()


# create entity handler
entity_handler = handler.EntityHandler()

# create a bunch of entities
entity_handler.add_entity(
    entity.Entity("player", [100, 100], [100, 100], pygame.image.load("red.png"))
)
entity_handler.add_entity(
    entity.Entity("player", [100, 100], [200, 200], pygame.image.load("red.png"))
)
entity_handler.add_entity(
    entity.Entity("player", [100, 100], [300, 300], pygame.image.load("red.png"))
)
entity_handler.add_entity(
    entity.Entity("player", [100, 100], [400, 400], pygame.image.load("red.png"))
)
entity_handler.add_entity(
    entity.Entity("player", [100, 100], [500, 500], pygame.image.load("red.png"))
)


PLAYER = entity.Entity("player", [100, 100], 
            [100, 100], pygame.image.load("red.png"))
entity_handler.add_entity(PLAYER)




# ------------------------------

block = pygame.image.load("red.png")

# ------------------------------


delta = 1
current = 0
previous = 0


current = time.time()
previous = time.time()

running = True
while running:
    # pause the game for a certain amount of time
    clock.tick(FPS)

    # update the clock
    current = time.time()
    delta = current - previous
    previous = current

    inputhandler.update_hardware()
    # handle events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            # keyboard press
            inputhandler.update_keyboard_down(e)
        elif e.type == pygame.KEYUP:
            # keyboard release
            inputhandler.update_keyboard_up(e)
        elif e.type == pygame.MOUSEMOTION:
            # mouse movement
            inputhandler.update_mouse_pos(e)
        elif e.type == pygame.MOUSEWHEEL:
            # mouse scroll
            inputhandler.update_mouse_scroll(e)
        elif e.type == pygame.MOUSEBUTTONDOWN:
            # mouse press
            inputhandler.update_mouse_press(e)
        elif e.type == pygame.MOUSEBUTTONUP:
            # mouse release
            inputhandler.update_mouse_release(e)

    # draw everything
    window.fill(BACKGROUND)

    # update the game
    entity_handler.update()

    print(delta)

    # udpate stuff HERE
    if inputhandler.is_key_pressed(pygame.K_d):
        PLAYER.position[0] += 10

    # render the game
    entity_handler.render(window)

    # update the window
    pygame.display.update()

# ------------------------------
pygame.quit()
