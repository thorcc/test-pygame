import pygame
from scene import Scene

class Meny(Scene):
    def __init__(self, bredde: int, høyde: int, menyvalg: list):
        super().__init__(bredde, høyde)
        self.tittel_font = pygame.font.SysFont("Arial", 64)
        self.tekst_font = pygame.font.SysFont("Arial", 32)
        self.menyvalg = menyvalg
        self.peker_posisjon = 0

    def håndter_input(self, hendelser: list):
        for hendelse in hendelser:
            if hendelse.type == pygame.KEYDOWN:
                if hendelse.key == pygame.K_DOWN:
                    self.peker_posisjon += 1
                    if self.peker_posisjon >= len(self.menyvalg):
                        self.peker_posisjon = 0
                elif hendelse.key == pygame.K_UP:
                    self.peker_posisjon -= 1
                    if self.peker_posisjon < 0:
                        self.peker_posisjon = len(self.menyvalg) - 1
                elif hendelse.key == pygame.K_RETURN:
                    print(f"Valg: {self.peker_posisjon}")
                    self.menyvalg[self.peker_posisjon]["handling"]()


    def tegn(self, vindu):
        self.overflate.fill("black")

        for i, valg in enumerate(self.menyvalg):
            valgtekst = self.tekst_font.render(valg["tekst"], True, "white")
            self.overflate.blit(valgtekst, (75, 100 + i * 50))

        peker = self.tekst_font.render(">", True, "white")
        self.overflate.blit(peker, (50, 100 + self.peker_posisjon * 50))

        vindu.blit(self.overflate, self.ramme)
