# Import frameworku Pygame
import pygame

# Inicializace frameworku
pygame.init()

# Vytvoření okna o rozměrech 500 x 500
screen = pygame.display.set_mode((500, 500))
# Proměnná running - kontroluje běh aplikace
running = True

# Smyčka pro herní cyklus
while running:
    # Cyklus pro odchytávání událostí
    for event in pygame.event.get():
        # Při odchycení události pygame.QUIT (uzavření okna)
        if event.type == pygame.QUIT:
            # Proměnná running nastavena na False
            running = False

    # Nastavení barvy výplně okna - bílé pozadí
    screen.fill((255, 255, 255))
    # Vytvoření kruhového objektu v oblasti okna (screen), v modré barvě (0, 0, 255),
    # se středem (250, 250) a poloměrem (75)
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    # Vytvoření obdélníku
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(5, 5, 100, 50))
    # Provede obnovení (aktualizaci) okna
    pygame.display.flip()

# Ukončení aplikace
pygame.quit()