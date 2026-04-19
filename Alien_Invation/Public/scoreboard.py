import pygame.font
class Scoreboard:
    """显示得分信息的类"""
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.stats = ai_game.game_stats
        #字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)
        self.prep_score()

    def prep_score(self):
        """将得分渲染为图像"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,True,
                                    self.text_color,self.settings.bg_color)
        #在屏幕右上角显示评分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def show_score(self):
        """绘制玩家得分"""
        self.screen.blit(self.score_image,self.score_rect)