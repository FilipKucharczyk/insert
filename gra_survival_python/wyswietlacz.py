import pygame
from ustawienia import *
def utworz_wyswietlacz():
    screen = pygame.display.set_mode((SZEROKOSC,WYSOKOSC))
    pygame.display.set_caption("Arena Survival")
    return screen

def narysuj_gracza(screen, gracz):
    screen.fill(CIEMNOSZARY)
    gracz.rysuj(screen)
    pygame.display.flip()