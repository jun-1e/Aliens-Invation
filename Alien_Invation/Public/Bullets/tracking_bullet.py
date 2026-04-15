from bullet import Bullet
import pygame

class Tracking_Bullet(Bullet):
    def __init__(self,ai_game,shooter):
        super().__init__(ai_game,shooter)
        self.rect = pygame.Rect(0,0,)

