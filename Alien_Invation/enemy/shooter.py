import pygame
from enemy.aliens import Alien
from Public.Bullets.homing_bullet import Homing_Bullet


class Shooter(Alien):
    """发射子弹的外星人"""
    def __init__(self,ai_game):
        """初始化外星人位置""" 
        super().__init__(ai_game)
        self.image = pygame.image.load('resource/Images/Shooter.bmp')
        self.rect = self.image.get_rect()
        self.bullets = pygame.sprite.Group()
        self.shooting_cooldown = self.settings.Shooter_cooldown
        self.cooldown = 0
        

    def shoot(self):
        """发射子弹"""
        self.cooldown+=1
        if self.cooldown >= self.shooting_cooldown:
            self.cooldown = 0
            
            new_Hbullet = Homing_Bullet(self.ai_game,self,
                            self.ai_game.playership.rect.center)
            self.bullets.add(new_Hbullet)


    def update(self):
        """更新外星人"""
        self.rect.x += self.settings.alien_speed * self.xdirection 

     
