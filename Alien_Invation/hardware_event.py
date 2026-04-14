import pygame
import sys
from settings import Settings

class Hardware_Event:
    def __init__(self,ai_game):
        self.ai_game = ai_game
        self.settings = Settings()
        self.screen = ai_game.screen

    def check_events(self):
        """侦听键盘和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
                
    def check_keydown_events(self,event):
        """响应按键"""
        if event.key == pygame.K_a:
            self.ai_game.playership.moving_left = True
        elif event.key == pygame.K_d:
            self.ai_game.playership.moving_right = True
        elif event.key == pygame.K_w:
            self.ai_game.playership.moving_up = True
        elif event.key == pygame.K_s:
            self.ai_game.playership.moving_down = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_j:
            self.ai_game.shooting = True
    
    def check_keyup_events(self,event):
        """响应松开"""
        if event.key == pygame.K_a:
            self.ai_game.playership.moving_left = False
        elif event.key == pygame.K_d:
            self.ai_game.playership.moving_right = False
        elif event.key == pygame.K_w:
            self.ai_game.playership.moving_up = False
        elif event.key == pygame.K_s:
            self.ai_game.playership.moving_down = False
        elif event.key == pygame.K_j:
            self.ai_game.shooting = False
        elif event.key == pygame.K_SPACE:
            self.ai_game.Pause = not self.ai_game.Pause
    
    def update_screen(self):
         #最近绘制的屏幕可见
            self.screen.fill(self.settings.bg_color)
            #绘制子弹
            for bullet in self.ai_game.playership.bullets.sprites():
                bullet.draw_bullet()
            
            self.ai_game.playership.blitme()           
            for alien in self.ai_game.aliens_fleet.sprites():
                alien.draw_alien()    
                
            pygame.display.flip()
    