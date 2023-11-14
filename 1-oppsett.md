# Oppsett

```python
import pygame

# Konstanter
BREDDE = 600
HOYDE = 400
FPS = 60

# Oppsett
pygame.init()
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

# Gameloop
while True:

    # Håndter input
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    

    pygame.display.flip()
    klokke.tick(FPS)

```
