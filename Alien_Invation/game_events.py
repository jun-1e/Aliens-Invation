from aliens import Alien
from random import randint
class Game_Events:
     def __init__(self,ai_game):
        self.ai_game = ai_game
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.alien = Alien(self.ai_game)
        self.randint = randint

     def _create_fleet(self):
        """创建外星人群"""
        #创建一个外星人，并计算一行可以容纳多少外星人
        self.ai_game.spawn_timer+=1
        if self.ai_game.spawn_timer >= self.settings.spawn_timer_set*50:            
            if len(self.ai_game.aliens_fleet) < self.settings.aliens_allowed:            
                for times in range(self.settings.create_max_attempts):
                    #每个外星人都出现在屏幕最上方随机位置
                    alien = Alien(self.ai_game)
                    alien.rect.x = self.randint(-20,self.settings.screen_width-alien.rect.width+20)
                    alien.rect.y = 0              
                    if not any(alien.rect.colliderect(existing_alien.rect) 
                            for existing_alien in self.ai_game.aliens_fleet):                    
                        self.ai_game.aliens_fleet.add(alien)
                        break
            self.ai_game.spawn_timer = 0

     def _check_collisions(self):
        """检查子弹和外星人碰撞"""
        for alien in self.ai_game.aliens_fleet.copy():
            if alien.rect.top > self.settings.screen_height :
                self.ai_game.aliens_fleet.remove(alien)
            for bullet in self.ai_game.playership.bullets.copy():
                if bullet.rect.colliderect(alien.rect):
                    bullet.kill()
                    alien.kill()
                    print("hit")
                    break
        #检查外星人和墙壁碰撞
        for alien in self.ai_game.aliens_fleet.copy():
            if (alien.rect.right >= self.ai_game.screen.get_rect().right or 
                alien.rect.left <= self.ai_game.screen.get_rect().left):
                alien.xdirection *= -1
                break
        #检查外星人和飞船碰撞
        for alien in self.ai_game.aliens_fleet.copy():
            if alien.rect.colliderect(self.ai_game.playership.rect):
                self.ai_game.playership.life -= self.settings.crash_damage
                alien.kill()