

import pygame

window_size = [1280, 720]
fps = 30

# you can change this to change the color
color = [255, 255, 255, 255]



window = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

running = True

while running:
    
    clock.tick(fps)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            
    window.fill(color)

    # draw random stuff here
    pygame.draw.circle(window, (255, 0, 0), (100, 100), 50)
    

    # update the display
    pygame.display.update()




