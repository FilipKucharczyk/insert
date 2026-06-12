import pygame
from ustawienia import *
def utworz_wyswietlacz():
    screen = pygame.display.set_mode((SZEROKOSC,WYSOKOSC))
    pygame.display.set_caption("Arena Survival")
    return screen

def narysuj(screen, gracz, lista_wrogow, lista_pociskow):
    screen.fill(CIEMNOSZARY)
    gracz.rysuj(screen)
    for wrog in lista_wrogow:
        wrog.rysuj(screen) 
    for pocisk in lista_pociskow:
        pocisk.rysuj(screen)
    pygame.display.flip()