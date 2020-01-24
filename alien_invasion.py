#!/usr/bin/env python
# -*- coding: utf-8 -*-
# purpose : 创建一系列整个游戏都要用到的对象
import sys
import pygame

from ship import Ship
from settings import Settings
import game_functions as gf
from pygame.sprite import Group

def update_bullets(ai_settings, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if (bullet.rect.bottom <= 0 or 
            bullet.rect.left <= 0 or
            bullet.rect.top >= ai_settings.screen_height or
            bullet.rect.right >= ai_settings.screen_width):
                
            bullets.remove(bullet)

def run_game():
    #init game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invasion")
    
    ship = Ship(ai_settings, screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    
    
    # begin to game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        update_bullets(ai_settings, bullets)
        #print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, bullets)
        
        
run_game()


