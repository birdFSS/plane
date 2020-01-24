#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings       
        
        #设置飞船图片
        self.image = pygame.image.load('images/ship1.bmp')
        self.rect  = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #设置飞船初始位置为整个屏幕的中间底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #在飞船的属性center中存放小数
        self.center = float(self.rect.centerx)
        
        #移动标志，保证按稳能够一直右移
        self.moving_right = False;
        self.moving_left = False;
        
        
    def update(self): 
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
            
        #根据self.center更新rect对象
        #self.rect.centerx只保存self.center的整数部分       
        self.rect.centerx = self.center
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
