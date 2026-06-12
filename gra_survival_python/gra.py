import pygame
from Gracz import *
from Wrog import * # Importujemy nową klasę
from ustawienia import *
from wyswietlacz import *
from Wrog import *
from Pocisk import *

pygame.init()
screen = utworz_wyswietlacz()
clock = pygame.time.Clock()

Moj_gracz = Gracz(SZEROKOSC/2, WYSOKOSC/2)

lista_wrogow = []
Spawn_Wroga = pygame.USEREVENT + 1
pygame.time.set_timer(Spawn_Wroga, 5000)

lista_pociskow = []
Spawn_Pocisku = pygame.USEREVENT + 2
pygame.time.set_timer(Spawn_Pocisku, 500)

czy_strzal = True
running = True

while running:
    # --- ZDARZENIA ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == Spawn_Wroga:
            lista_wrogow.append(Wrog())
        if event.type == Spawn_Pocisku:
            czy_strzal = True
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        Moj_gracz.rusz('L')
    if keys[pygame.K_RIGHT]:
        Moj_gracz.rusz('P')
    if keys[pygame.K_UP]:
        Moj_gracz.rusz('G')
    if keys[pygame.K_DOWN]:
        Moj_gracz.rusz('D')
    
    # Tworzenie pociskow
    if czy_strzal:
        if keys[pygame.K_a]:
            lista_pociskow.append(Pocisk('L', Moj_gracz.rect.x, Moj_gracz.rect.y))
            czy_strzal = False
        elif keys[pygame.K_d]:
            lista_pociskow.append(Pocisk('P', Moj_gracz.rect.x, Moj_gracz.rect.y))
            czy_strzal = False
        elif keys[pygame.K_w]:
            lista_pociskow.append(Pocisk('G', Moj_gracz.rect.x, Moj_gracz.rect.y))
            czy_strzal = False
        elif keys[pygame.K_s]:
            lista_pociskow.append(Pocisk('D', Moj_gracz.rect.x, Moj_gracz.rect.y))
            czy_strzal = False
    
    for wrog in lista_wrogow:
        wrog.gon(Moj_gracz.rect)
        
    for pocisk in lista_pociskow:
        pocisk.rusz()
    
    narysuj_gre(screen, Moj_gracz, lista_wrogow, lista_pociskow)
    clock.tick(FPS)
    
