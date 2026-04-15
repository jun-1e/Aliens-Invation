import pygame
from enemy.aliens import Alien
from enemy.shooter import Shooter
from random import randint

class Game_Events:
     def __init__(self,ai_game):
        self.ai_game = ai_game
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.alien = Alien(self.ai_game)
        self.randint = randint

     def get_spawn_loc(self,alien_type):
         """获得新创建的外星人位置"""
         alien_type.rect.x = self.randint(-20,self.settings.screen_width-alien_type.rect.width+20)
         alien_type.rect.y = 0 

     def _create_fleet(self):
        """创建外星人群"""
        #根据run_game循环次数创建一个外星人，并受到最大数量限制
        self.ai_game.spawn_timer+=10
        if self.ai_game.spawn_timer >= self.settings.spawn_timer_set*50:            
            if len(self.ai_game.aliens_fleet) < self.settings.aliens_allowed:            
                for times in range(self.settings.create_max_attempts):
                    #每个外星人都出现在屏幕最上方随机位置
                    alien_type = randint(0,1)
                    if alien_type:
                        alien = Alien(self.ai_game)
                        self.get_spawn_loc(alien)
                    else:
                        alien = Shooter(self.ai_game)
                        self.get_spawn_loc(alien)
                    #新创建的外星人不会与目前已有的外星人重叠
                    if not any(alien.rect.colliderect(existing_alien.rect) 
                            for existing_alien in self.ai_game.aliens_fleet):                    
                        self.ai_game.aliens_fleet.add(alien)
                        break
            self.ai_game.spawn_timer = 0

     def _check_collisions(self):
        """检查子弹和外星人碰撞"""
        for alien in self.ai_game.aliens_fleet.copy():
            for bullet in self.ai_game.playership.bullets.copy():
                if bullet.rect.colliderect(alien.rect):
                    bullet.kill()
                    alien.kill()
                    print("hit")
                    break
        #检查外星人和墙壁碰撞
        for alien in self.ai_game.aliens_fleet.copy():
            if alien.rect.bottom >= self.ai_game.screen.get_rect().bottom+20:
                self.ai_game.playership.life -= self.settings.EnemyInvade_damage
                print('-1')
            if (alien.rect.right >= self.ai_game.screen.get_rect().right+20 or 
                alien.rect.left <= self.ai_game.screen.get_rect().left-20):
                alien.xdirection *= -1
                break
        #检查外星人和飞船碰撞
        for alien in self.ai_game.aliens_fleet.copy():
            if alien.rect.colliderect(self.ai_game.playership.rect):
                self.ai_game.playership.life -= self.settings.crash_damage
                alien.kill()
    
     def check_life_change(self):
        """检查玩家生命值变化"""
        if self.ai_game.playership.life <= 0:
            self.ai_game.Dead = True 

     def update_screen(self):
        """绘制屏幕"""
        self.screen.fill(self.settings.bg_color)
        #绘制子弹
        for bullet in self.ai_game.playership.bullets.sprites():
            bullet.draw_player_bullet()
        #绘制玩家飞船    
        self.ai_game.playership.blitme() 
        #绘制外星人          
        for alien in self.ai_game.aliens_fleet.sprites():
            alien.draw_alien()    
        #更新屏幕                
        pygame.display.flip()
     
     def draw_pause_lay(self):
         overlay = pygame.Surface((self.settings.screen_width,self.settings.screen_height),
                                  pygame.SRCALPHA)
         overlay.fill((0,0,0,2))
         self.screen.blit(overlay,(0,0))
         pygame.display.flip()