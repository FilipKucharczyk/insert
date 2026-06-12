import random
import pygame
from ustawienia import *

class Pocisk:
    def __init__(self, kierunek, x, y):
        self.rect = pygame.Rect(x+20, y+20, 10, 10)
        self.color = (255, 255, 0)
        self.predkosc = 10
        self.kierunek = kierunek
    
    def rysuj(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
         
    def rusz(self):
        strona = self.kierunek
        if(strona == 'L'):
            self.rect.x -= self.predkosc
        elif(strona == 'P'):
            self.rect.x += self.predkosc
        elif(strona == 'G'):
            self.rect.y -= self.predkosc
        elif(strona == 'D'):
            self.rect.y += self.predkosc