import pygame
from Gracz import *
from Wrog import * # Importujemy nową klasę
from ustawienia import *
from wyswietlacz import *
from Wrog import *

pygame.init()
screen = utworz_wyswietlacz()
clock = pygame.time.Clock()

Moj_gracz = Gracz(SZEROKOSC/2, WYSOKOSC/2)
lista_wrogow = []
Spawn_Wroga = pygame.USEREVENT + 1
pygame.time.set_timer(Spawn_Wroga, 5000)
running = True

while running:
    # --- ZDARZENIA ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == Spawn_Wroga:
            lista_wrogow.append(Wrog())
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        Moj_gracz.rusz('L')
    if keys[pygame.K_RIGHT]:
        Moj_gracz.rusz('P')
    if keys[pygame.K_UP]:
        Moj_gracz.rusz('G')
    if keys[pygame.K_DOWN]:
        Moj_gracz.rusz('D')
    
    for wrog in lista_wrogow:
        wrog.gon_gracza(Moj_gracz.rect)
    
    narysuj(screen, Moj_gracz, lista_wrogow)
    clock.tick(FPS)
    
