####
#
# Zadania:
# 1. zapoznaj sie dokladnie z dzialaniem ponizszego przykladu
# 2. wprowadz mozliwosc poruszania postacia w grze za pomoca strzałek lub klawiszy 'AWSD'
# 3. zablokuj postaci mozliwosc wychodzenia poza krawedz widocznego okna
# 4. poszukaj w internecie informacji o funkcji pygame.key.get_pressed() i sprobuj
#   z jej uzyciem wprowadzic plynny ruch postaci

import pygame
import os

# centrowanie okna
os.environ["SDL_VIDEO_CENTERED"] = '1'

# inicjalizacja srodowiska pygame
pygame.init()

# tworzenie okna gry
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("My first game")
# kolory w pygame definiujemy zgodnie z formatem RGB
TEAL = (0, 128, 128)

# utworzenie obiektu zegara do regulacji FPS-ów
clock = pygame.time.Clock()

# wczytanie grafiki
player = pygame.image.load('./assets/crab.png').convert_alpha()

VEL = 5
player_position = 368, 268


def draw_window(crab):
    screen.fill(TEAL)       # wypelnienie tla
    screen.blit(player, (crab.x, crab.y))        # blit - rysowanie obrazu, tu przedstawiajacego postac
    pygame.display.flip()


def move(keys_pressed, crab):
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        if crab.x - VEL > 0:
            crab.x -= VEL
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        if crab.x + VEL + 64 < 800:     # 64 to szerokosc kraba
            crab.x += VEL
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        if crab.y - VEL > 0:
            crab.y -= VEL
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        if crab.y + VEL + 64 < 600:
            crab.y += VEL


def main():
    crab = pygame.Rect(368, 268, 64, 64)     # rectangle, zeby miec dostep do crab.x, crab.y
    # 64 to wymiary craba, a 368 i 268 to player_position
    # petla gry (game loop)
    running = True
    while running:
        clock.tick(30)  # liczba klatek na sekunde
        # obsluga zdarzen (event handling)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # klikniecie przycisku zamkniecia okna (X)
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        keys_pressed = pygame.key.get_pressed()
        move(keys_pressed, crab)
        draw_window(crab)

    pygame.quit()


if __name__ == '__main__':
    main()
