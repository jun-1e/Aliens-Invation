import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理子弹类"""
    def __init__(self,ai_game,shooter):
        """在飞船当前位置创建一个子弹对象"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color_Blue = (0,255,255)
        self.color_Red = (255,0,0)
        #在(0,0)处创建一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = shooter.rect.midtop
        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """向上移动子弹"""
        #更新子弹的准确位置
        self.y -= self.settings.bullet_speed
        self.x += self.settings.bullet_speed
        #更新表示子弹的rect位置
        self.rect.y = self.y
        #删除已消失的子弹
        if self.rect.bottom <= 0:
            self.kill() 
           
    def draw_player_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color_Blue,self.rect)
    def draw_enemy_bullet(self):
        pygame.draw.circle(self.screen,self.color_Red,self.rect.midtop,5)