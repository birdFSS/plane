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

class Direction():
    
    def __init__(self, speed_x, speed_y):
        self.x = speed_x
        self.y = speed_y


class Bullet(Sprite):
    """一个对子弹进行管理的类"""
    
    def __init__(self, ai_settings, screen, ship, direction):
        super(Bullet, self).__init__()
        self.screen = screen
        
        if abs(direction.x) > abs(direction.y):
            self.rect = pygame.Rect(0,0,ai_settings.bullet_height,
                                    ai_settings.bullet_width)
        else:       
            self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
                                    ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #设置子弹的飞行方向和速度
        self.direction = direction
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        self.x += self.speed_factor * self.direction.x
        self.rect.x = self.x
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor * self.direction.y
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
