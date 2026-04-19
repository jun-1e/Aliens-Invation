import pygame
from enemy.aliens import Alien
from enemy.shooter import Shooter
from Public.scoreboard import Scoreboard
from random import randint

class Game_Events:
     def __init__(self,ai_game):
        self.ai_game = ai_game
        self.settings = ai_game.settings
        
        self.screen = ai_game.screen
        self.alien = Alien(self.ai_game)
        self.randint = randint
        self.aliens_fleet = ai_game.aliens_fleet
        self.playership = ai_game.playership
        self.game_stats = ai_game.game_stats
        self.scoreboard = Scoreboard(self.ai_game)
        self.PLB_rect = pygame.Rect(self.settings.screen_width-self.settings.PLB_width-50,
                                                self.settings.screen_height - 20,
                                                self.settings.PLB_width,
                                                self.settings.PLB_height)
        self.current_PLB_rect = self.PLB_rect.copy()
        
        

     def get_spawn_loc(self,alien_type):
         """获得新创建的外星人位置"""
         alien_type.rect.x = self.randint(0,self.settings.screen_width-alien_type.rect.width)
         alien_type.rect.y = 0 

     def draw_life_Bar(self):
        """绘制血条"""        
        pygame.draw.rect(self.screen,self.settings.color_dark_RED,self.PLB_rect)
        self.current_PLB_rect.width =int(self.PLB_rect.width*(self.ai_game.playership.life/self.settings.life_limit))
        pygame.draw.rect(self.screen,self.settings.color_RED,self.current_PLB_rect)
    
     
     def _create_fleet(self):
        """创建外星人群"""
        #根据run_game循环次数创建一个外星人，并受到最大数量限制
        self.ai_game.spawn_timer+=10
        if self.ai_game.spawn_timer >= self.settings.spawn_timer_set*50:            
            if len(self.aliens_fleet) < self.settings.aliens_allowed:            
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
                            for existing_alien in self.aliens_fleet):                    
                        self.aliens_fleet.add(alien)
                        break
            self.ai_game.spawn_timer = 0

     def _check_collisions(self):
        """检查外星人碰撞相关信息"""        
        # 碰撞检测，删除子弹和被击中的外星人
        collisions = pygame.sprite.groupcollide(
            self.playership.bullets, self.aliens_fleet,True,True)
        if collisions:
            total_score = 0
            for bullet, aliens in collisions.items():
                for alien in aliens:
                    total_score += alien.score   
                self.game_stats.score += total_score
                self.scoreboard.prep_score()
        #检查外星人和墙壁碰撞
        for alien in self.aliens_fleet.copy():
            if alien.rect.bottom >= self.ai_game.screen.get_rect().bottom+20:
                self.ai_game.playership.life -= self.settings.EnemyInvade_damage
                alien.kill()
                #如果外星人碰到侧面的墙壁则则改变水平运动方向
            if (alien.rect.right >= self.screen.get_rect().right+20 or 
                alien.rect.left <= self.screen.get_rect().left-20):
                alien.xdirection *= -1
                break
        #检查外星人和飞船碰撞
        for alien in self.aliens_fleet.copy():
            if alien.rect.colliderect(self.playership.rect):
                self.playership.life -= self.settings.crash_damage
                alien.kill()
        #检查Shooter型外星人的子弹与玩家飞船的碰撞
        for alien in self.aliens_fleet.sprites():
            if type(alien) == Shooter:
                for bullet in alien.bullets.sprites():
                    if bullet.rect.colliderect(self.playership.rect):
                        self.playership.life -= 5
                        bullet.kill()

    
     def check_life_change(self):
        """检查玩家生命值变化"""    
        if self.playership.life <= 0:
            self.ai_game.Dead = True 


     def update_screen(self):
        """绘制屏幕"""
        #Shooter类敌人发射子弹
        for alien in self.aliens_fleet.copy():
            if type(alien) == Shooter:
                alien.shoot()
        self.screen.fill(self.settings.bg_color)
        #绘制子弹
        for bullet in self.playership.bullets.sprites():
            bullet.draw_player_bullet()
        #绘制玩家飞船和血量    
        self.playership.blitme()
        self.draw_life_Bar()
        self.scoreboard.show_score()        
        #绘制外星人          
        for alien in self.aliens_fleet.sprites():
            alien.draw_alien() 
            if type(alien) == Shooter:
                for bullet in alien.bullets.sprites():
                    bullet.update()
                    bullet.draw_Hbullet()   
        
     
     def draw_pause_lay(self):
         """绘制暂停界面"""
         while self.ai_game.transparency_count < self.settings.Pause_transparency:
            overlay = pygame.Surface((self.settings.screen_width,self.settings.screen_height),
                                    pygame.SRCALPHA)
            overlay.fill((0,0,0,2))
            self.screen.blit(overlay,(0,0))
            pygame.display.flip()
            self.ai_game.transparency_count+=1
         