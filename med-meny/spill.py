import pygame
from scene import Scene

class Spill(Scene):
    def __init__(self, bredde: int, høyde: int, avslutt: callable):
        super().__init__(bredde, høyde)
        self.figur_bilde = pygame.image.load("bilder/spiller.png")
        self.figur_ramme = self.figur_bilde.get_rect()
        self.avslutt = avslutt
    
    def håndter_input(self, hendelser: list):
        for hendelse in hendelser:
            if hendelse.type == pygame.KEYDOWN:
                if hendelse.key == pygame.K_DOWN:
                    self.figur_ramme.y += 1
                elif hendelse.key == pygame.K_UP:
                    self.figur_ramme.y -= 1
                elif hendelse.key == pygame.K_LEFT:
                    self.figur_ramme.x -= 1
                elif hendelse.key == pygame.K_RIGHT:
                    self.figur_ramme.x += 1
                elif hendelse.key == pygame.K_ESCAPE:
                    self.avslutt()
                    

    def tegn(self, vindu):
        self.overflate.blit(self.figur_bilde, self.figur_ramme)

        vindu.blit(self.overflate, self.ramme)