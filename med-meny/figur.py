import pygame

class Figur():
    def __init__(self, x: int, y: int, bildesti: str):
        self.bilde = pygame.image.load(bildesti).convert_alpha()
        self.ramme = self.bilde.get_rect()

        self.ramme.x = x
        self.ramme.y = y

    def flytt(self, dx: int, dy: int):
        self.ramme.x += dx
        self.ramme.y += dy

    def tegn(self, overflate: pygame.Surface):
        overflate.blit(self.bilde, self.ramme)