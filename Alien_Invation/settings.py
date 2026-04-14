class Settings:
    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width = 1600
        self.screen_height = 1000
        self.bg_color = (255,255,255) #设置背景颜色
        #飞船设置
        self.ship_speed = 20.0
        self.lifes_limit = 5
        #子弹设置
        self.bullet_speed = 10.0
        self.bullet_width =5
        self.bullet_height = 20
        self.bullet_color = (60,60,60)
        self.bullet_cooldown = 200
        self.bullets_allowed = 9999
        #外星人设置
        self.aliens_allowed = 20
        self.create_max_attempts = 5
        self.alien_speed = 2.0
        self.enemy_bullet_damage = 1
        self.crash_damage = 2
        self.spawn_timer_set = 2