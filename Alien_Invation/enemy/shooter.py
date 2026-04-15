import pygame
from enemy.aliens import Alien


class Shooter(Alien):
    """发射子弹的外星人"""
    def __init__(self,ai_game):
        """初始化外星人位置""" 
        super().__init__(ai_game)
        self.image = pygame.image.load('resource/Images/Shooter.bmp')
        self.rect = self.image.get_rect()
        self.shooting_cooldown = self.settings.Shooter_cooldown
        

    def shoot(self):
        """发射子弹"""
        pass


    def update(self):
        """更新外星人"""
        self.rect.x += self.settings.alien_speed * self.xdirection 

     
