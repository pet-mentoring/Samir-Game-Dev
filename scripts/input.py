import pygame

# ------------------------------------------------ #
# hardware data -- input [mouse]
# ------------------------------------------------ #

MOUSE_POS = [0, 0]
MOUSE_MOVE = [0, 0]
MOUSE_BUTTONS = [False, False, False]
MOUSE_PRESSED = set()
MOUSE_SCROLL = [0, 0]
MOUSE_SCROLL_POS = [0, 0]


def update_mouse_pos(event):
    """Update mouse position."""
    MOUSE_MOVE[0], MOUSE_MOVE[1] = event.rel
    MOUSE_POS[0], MOUSE_POS[1] = event.pos


def update_mouse_press(event):
    """Update mouse button press."""
    if 3 < event.button > 1:
        return
    MOUSE_BUTTONS[event.button - 1] = True
    MOUSE_PRESSED.add(event.button - 1)


def update_mouse_release(event):
    """Update mouse button release."""
    # in case of scrolling
    if 3 < event.button > 1:
        return
    MOUSE_BUTTONS[event.button - 1] = False


def update_mouse_scroll(event):
    """Update mouse scroll."""
    MOUSE_SCROLL_POS[0] += event.precise_x
    MOUSE_SCROLL_POS[1] += event.precise_y
    MOUSE_SCROLL[0], MOUSE_SCROLL[1] = event.precise_x, event.precise_y


# ------------------------------------------------ #
# hardware data -- input [keyboard]
# ------------------------------------------------ #

KEYBOARD_KEYS = {}
KEYBOARD_PRESSED = set()

# ensure that the error does not occur
for i in range(0, 3000):
    KEYBOARD_KEYS[i] = False


def update_keyboard_down(event):
    """Update keyboard key press."""
    KEYBOARD_KEYS[event.key] = True
    KEYBOARD_PRESSED.add(event.key)


def update_keyboard_up(event):
    """Update keyboard key release."""
    KEYBOARD_KEYS[event.key] = False


# ------------------------------------------------ #
# hardware data -- input [key + mouse]
# ------------------------------------------------ #


def update_hardware():
    """Updates the mouse"""
    global MOUSE_SCROLL
    # print("DEBUG:", MOUSE_PRESSED, KEYBOARD_PRESSED)
    MOUSE_PRESSED.clear()
    MOUSE_SCROLL = [0, 0]
    KEYBOARD_PRESSED.clear()


def get_mouse_rel():
    """Returns mouse position."""
    return (
        MOUSE_POS[0] / WSIZE[0] * FSIZE[0],
        MOUSE_POS[1] / WSIZE[1] * FSIZE[1],
    )


def get_mouse_abs():
    """Returns mouse position."""
    return (MOUSE_POS[0], MOUSE_POS[1])


def is_mouse_pressed(button):
    """Returns if mouse button is pressed."""
    return MOUSE_BUTTONS[button]


def is_mouse_clicked(button):
    """Returns if mouse button is clicked."""
    return button in MOUSE_PRESSED


def is_key_pressed(key):
    """Returns if key is pressed."""
    if not key in KEYBOARD_KEYS:
        KEYBOARD_KEYS[key] = False
    return KEYBOARD_KEYS[key]


def is_key_clicked(key):
    """Returns if key is clicked."""
    return key in KEYBOARD_PRESSED
