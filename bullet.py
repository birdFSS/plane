#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename : bullet.py
# purpose : 子弹类
# author : birdFSS
# Date : 2020/01/24
# change log 
# 2020/01/24 create this file
#
#

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对子弹进行管理的类"""
    
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
