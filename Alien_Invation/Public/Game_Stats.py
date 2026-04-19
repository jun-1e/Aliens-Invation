import pygame
from Public.settings import Settings

class game_stats:
    """管理游戏内数值变化的类"""
    def __init__(self):
        self.setting = Settings
        self.score = 0
