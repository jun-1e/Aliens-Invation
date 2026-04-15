import pygame
from Public.Bullets.bullet import Bullet

class Ship:
    """管理飞船的类"""
    def __init__(self,ai_game):
        """初始化飞船位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.ai_game = ai_game
        self.last_shot_time = 0
        self.bullets = pygame.sprite.Group()
        self.life_limit = self.settings.life_limit
        self.life = self.life_limit

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('resource/Images/shiip_2 (2).bmp')
        self.rect = self.image.get_rect()

        #每艘飞船都出现在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #移动标志（初始值为False）
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right+10:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left-10:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > self.screen_rect.top-10:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom+10:
            self.y += self.settings.ship_speed
        self.rect.x = self.x
        self.rect.y = self.y   

    def update_bullet(self):
        self.bullets.update()
    
    def fire_bullet(self):
        if self.ai_game.shooting and len(self.bullets) < self.settings.bullets_allowed:
            current_time = pygame.time.get_ticks()
            """创建子弹并加入bullets"""
            if current_time - self.last_shot_time > (
                self.settings.bullet_cooldown and self.ai_game.shooting):
                new_bullet= Bullet(self.ai_game,self)
                self.bullets.add(new_bullet)
                self.last_shot_time = current_time
    
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    
