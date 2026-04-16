import pygame
from Public.settings import Settings
from pygame.sprite import Sprite

class Homing_Bullet(Sprite):
    def __init__(self,ai_game,shooter,target_pos):
        super().__init__()
        self.setting = Settings()
        self.screen = ai_game.screen
        self.rect = pygame.Rect(0,0,self.setting.bullet_width,
                                self.setting.bullet_width)
        self.rect.center = shooter.rect.center
        #获取速度向量
        start_pos = pygame.math.Vector2(self.rect.center)
        target = pygame.math.Vector2(target_pos)
        direction = (target-start_pos).normalize()
        self.velocity = direction * self.setting.bullet_speed
        
        self.pos = pygame.math.Vector2(self.rect.center)

    def update(self):
        """更新子弹位置"""
        self.pos += self.velocity
        self.rect.center = (int(self.pos.x),int(self.pos.y))
        #删除超出屏幕的子弹
        if (self.rect.right < 0 or self.rect.left > self.setting.screen_width or
            self.rect.top > self.setting.screen_height or self.rect.bottom < 0):
            self.kill()
            
    def draw_Hbullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.circle(self.screen,self.setting.color_RED,self.rect.center,5)
        

