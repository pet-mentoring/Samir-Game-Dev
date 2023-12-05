

import pygame


# ------------------ EntityHandler ------------------

class EntityHandler:
    def __init__(self):
        # the list of entities
        self.entities = {}

    def update(self):
        for eid in self.entities:
            entity = self.entities[eid]

            # check if entity is alive
            if not entity.alive:
                # remove the entity
                del self.entities[eid]
                continue
            
            # update the entity
            entity.update()
    
    def render(self, surface):

        for eid in self.entities:
            entity = self.entities[eid]
            # render the entity
            entity.render(surface)

    def add_entity(self, entity):
        self.entities[entity._id] = entity
    
    def remove_entity(self, entity):
        del self.entities[entity._id]



