import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """管理外星人类"""
    def __init__(self,ai_game):
        """初始化外星人位置""" 
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.ai_game = ai_game
        self.aliens_fleet = []
        self.spawn_timer = 0
        self.xdirection = 1
        #加载外星人图像并获取其外接矩形
        self.image = pygame.image.load('resource/Images/shiip_2 (2).bmp')
        self.rect = self.image.get_rect()

    
    def update(self):
        """更新外星人"""
        self.rect.x += self.settings.alien_speed * self.xdirection
        self.rect.y += self.settings.alien_speed * 0.5


    def draw_alien(self):
        """在屏幕上绘制外星人"""
        self.screen.blit(self.image,(self.rect.x,self.rect.y))
            
        
