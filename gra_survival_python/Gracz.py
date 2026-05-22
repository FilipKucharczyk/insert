import pygame
from insert.gra_survival_python.ustawienia import *

class Gracz:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, ROZMIAR, ROZMIAR)
        self.color = KOLORGRACZA
        self.predkosc = PREDKOSCGRACZA
    
    def rysuj(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
       
    def rusz(self, strona):
        if(strona == 'L'):
            self.rect.x -= self.predkosc
        elif(strona == 'P'):
            self.rect.x += self.predkosc
        elif(strona == 'G'):
            self.rect.y -= self.predkosc
        elif(strona == 'D'):
            self.rect.y += self.predkosc
        
        if self.rect.left < 0 :
            self.rect.x = 0
            