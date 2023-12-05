
# importing the pygame module
import pygame


# the entity class
class Entity:
    # class specific variable
    __ENTITY_ID = 1

    def __init__(self, name: str, area: list, position: list, image: pygame.Surface):
        # set all variables
        self.name = name
        self.area = pygame.Rect(position, area)
        self.position = position
        self.image = image
        self.alive = True

        # give it a unique id
        self._id = Entity.__ENTITY_ID
        # increase by 1 so we don't have duplicate ids
        Entity.__ENTITY_ID += 1
    
    def update(self):
        pass

    def render(self, surface):
        surface.blit(self.image, self.position)



