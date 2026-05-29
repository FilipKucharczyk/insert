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
        
    