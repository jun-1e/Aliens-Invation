import pygame
from Public.settings import Settings
from player_ship import Ship
from Events.hardware_event import Hardware_Event
from Events.game_events import Game_Events

class AlienInvasion:
    """管理游戏资源和行为类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        
        self.transparency_count = 0
        self.spawn_timer = 0
        self.clock = pygame.time.Clock()
        self.settings = Settings()     
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("gametest")
        #初始化游戏内容
        self.Pause = False
        self.Dead = False
        self.shooting = False
        self.bullets = pygame.sprite.Group()
        self.aliens_fleet = pygame.sprite.Group()
        self.playership = Ship(self)
        self.event = Game_Events(self) 
        self.hardware_event = Hardware_Event(self)
        self.TESTBUTTOM = pygame.Rect(400,250,self.screen.get_width()/2,self.screen.get_height()/2)
        self.buttom_color = (0,0,0)
        
        
    def run_game(self):
        """开始游戏主循环"""
        while True:
            self.hardware_event.check_events()
            self.event.check_life_change() 

            if not self.Dead:
                if not self.Pause:                           
                    self.playership.update()
                    self.playership.fire_bullet()
                    self.playership.update_bullet()
                    self.event._check_collisions()
                    self.event._create_fleet()
                    self.aliens_fleet.update()
                    self.event.update_screen()               
                    self.clock.tick(60) #设置帧率
                elif self.Pause:                    
                    while self.transparency_count < self.settings.Pause_transparency:
                        self.event.draw_pause_lay()
                        self.transparency_count+=1
                        pygame.draw.rect(self.screen,self.buttom_color,self.TESTBUTTOM)
            elif self.Dead:
                while self.transparency_count < self.settings.Pause_transparency:
                    self.event.draw_pause_lay()
                    self.transparency_count+=1
                

if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai=AlienInvasion()
    ai.run_game()