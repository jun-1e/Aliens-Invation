import pygame
from Public.settings import Settings
class Button:
    def __init__(self,pos_x,pos_y,width,height):
        self.setting = Settings()
        self.button_color = self.setting.Button_color_default
        self.rect = pygame.Rect(pos_x,pos_y,width,height)

    def button_events(self):
        """按钮行为"""
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.button_color = self.setting.Button_color_check     
        else:
            self.button_color = self.setting.Button_color_default
            
    def draw_button(self,ai_game):
        """绘制按钮"""
        pygame.draw.rect(ai_game.screen,self.button_color,self.rect)
        