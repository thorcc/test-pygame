import pygame

class Scene():
    def __init__(self, bredde: int, høyde: int):
        self.overflate = pygame.Surface((bredde, høyde))
        self.ramme = self.overflate.get_rect()

