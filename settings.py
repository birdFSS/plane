#!/usr/bin/env python
#2020-01-23  birdFSS  <ffhbird@gmail.com>
#purpose : 配置信息，设置游戏的各项基本参数
#change log : create this file
#pur

class Settings():
#存储《外星人入侵》的所有设置的类
    def __init__(self):
        #初始化游戏的设置
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        
        
        #设置子弹属性
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3
        
