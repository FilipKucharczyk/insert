import pygame
from ustawienia import *

def utworz_wyswietlacz():
    screen = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
    pygame.display.set_caption("Arena Survival")
    return screen

<<<<<<< HEAD
def narysuj(screen, gracz, lista_wrogow):
=======
# dodajemy listę wrogów
def narysuj_gre(screen, gracz, lista_wrogow):
>>>>>>> 17a74ac (Gon gracza)
    screen.fill(CIEMNOSZARY)
    
    # Rysowanie gracza
    gracz.rysuj(screen)
<<<<<<< HEAD
    for wrog in lista_wrogow:
        wrog.rysuj(screen) 
=======
    
    # Rysowanie wrogów
    for wrog in lista_wrogow:
        wrog.rysuj(screen)
        
>>>>>>> 17a74ac (Gon gracza)
    pygame.display.flip()