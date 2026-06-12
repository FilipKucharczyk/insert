import random
import pygame
from ustawienia import *

class Wrog:
    def __init__(self):
        x = random.choice([100+0-ROZMIAR, SZEROKOSC+ROZMIAR])
        y = random.randint(100+0, WYSOKOSC)
        self.rect = pygame.Rect(x, y, ROZMIAR, ROZMIAR)
        self.color = KOLORWROGA
        self.predkosc = PREDKOSCWROGA
    
    def rysuj(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def gon(self, gracz_rectangle):
        if self.rect.x < gracz_rectangle.x:
            self.rect.x += self.predkosc
        if self.rect.x > gracz_rectangle.x:
            self.rect.x -= self.predkosc
        if self.rect.y < gracz_rectangle.y:
            self.rect.y += self.predkosc
        if self.rect.y > gracz_rectangle.y:
            self.rect.y -= self.predkosc
        
        
    def gon_gracza(self, gracz_rect):
        # Namierzanie gracza
        if self.rect.x < gracz_rect.x:
            self.rect.x += self.predkosc
        elif self.rect.x > gracz_rect.x:
            self.rect.x -= self.predkosc
            
        if self.rect.y < gracz_rect.y:
            self.rect.y += self.predkosc
        elif self.rect.y > gracz_rect.y:
            self.rect.y -= self.predkosc
