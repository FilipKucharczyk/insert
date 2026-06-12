import pygame
from ustawienia import *

def utworz_wyswietlacz():
    screen = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
    pygame.display.set_caption("Arena Survival")
    return screen

# dodajemy listę wrogów
def narysuj_gre(screen, gracz, lista_wrogow, lista_pociskow):
    screen.fill(CIEMNOSZARY)
    
    # Rysowanie gracza
    gracz.rysuj(screen)

    for wrog in lista_wrogow:
        wrog.rysuj(screen) 

    for pocisk in lista_pociskow:
        pocisk.rysuj(screen)

    # Rysowanie wrogów
    for wrog in lista_wrogow:
        wrog.rysuj(screen)

    pygame.display.flip()