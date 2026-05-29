import pygame
from ustawienia import *
def utworz_wyswietlacz():
    screen = pygame.display.set_mode((SZEROKOSC,WYSOKOSC))
    pygame.display.set_caption("Arena Survival")
    return screen

def narysuj(screen, gracz, lista_wrogow):
    screen.fill(CIEMNOSZARY)
    gracz.rysuj(screen)
    for wrog in lista_wrogow:
        wrog.rysuj(screen) 
    pygame.display.flip()