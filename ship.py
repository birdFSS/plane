#!/usr/bin/env python
# -*- coding: utf-8 -*-
# purpose : 包含Ship类
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
        self.rect.centery = self.screen_rect.bottom - 20
        
        #在飞船的属性center中存放小数
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        
        
        #移动标志，保证按稳能够一直右移
        self.moving_right = False;
        self.moving_left = False;
        self.moving_up = False;
        self.moving_down = False;
        
        
    def update(self): 
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
  
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.ai_settings.ship_speed_factor
            
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.ship_speed_factor
            
        #bottom 是下面，但是数值越大，越往下
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor    
        #根据self.center更新rect对象
        #self.rect.centerx只保存self.center的整数部分       
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
