import pygame
from meny import Meny
from spill import Spill


class Main():
    def __init__(self):
        # Konstanter
        self.BREDDE = 600
        self.HOYDE = 500
        self.FPS = 60

        # Oppsett
        pygame.init()
        self.vindu = pygame.display.set_mode((self.BREDDE, self.HOYDE))
        self.klokke = pygame.time.Clock()

        self.meny = Meny(self.BREDDE, self.HOYDE, [
            {"tekst": "Spill", "handling": self.vis_spill},
            {"tekst": "Avslutt", "handling": self.avslutt}
        ])
        self.spill = Spill(self.BREDDE, self.HOYDE, avslutt=self.vis_meny)

        self.aktiv_scene = self.meny

    def vis_spill(self):
        self.aktiv_scene = self.spill

    def vis_meny(self):
        self.aktiv_scene = self.meny

    def avslutt(self):
        pygame.quit()
        raise SystemExit

    def kjør(self):
        # Gameloop
        while True:

            # Håndter input
            hendelser = pygame.event.get()
            for hendelse in hendelser:
                if hendelse.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
            self.aktiv_scene.håndter_input(hendelser)

            # Tegn
            self.aktiv_scene.tegn(self.vindu)
            pygame.display.flip()
            self.klokke.tick(self.FPS)

main = Main()
main.kjør()