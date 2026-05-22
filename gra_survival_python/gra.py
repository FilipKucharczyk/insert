import pygame
from Gracz import *
from ustawienia import *
from wyswietlacz import *

pygame.init()
screen = utworz_wyswietlacz()

Moj_gracz = Gracz(SZEROKOSC/2, WYSOKOSC/2)

running = True

while running:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT):
                Moj_gracz.rusz('L')
            
    
    narysuj_gracza(screen, Moj_gracz)