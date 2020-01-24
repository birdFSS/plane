#!/usr/bin/env python
# -*- coding: utf-8 -*-
# purpose : 游戏的控制逻辑，通过check_events来处理发生的事件
import sys
import pygame
from bullet import Bullet, Direction


def fire_bullet(ai_settings, screen, ship, bullets, Direction):
    if len(bullets) < ai_settings.bullet_allowed :
        new_bullet = Bullet(ai_settings, screen, ship, Direction)
        bullets.add(new_bullet)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_down = True 
        
    #从不同方向发射子弹
    elif event.key == pygame.K_i:
        direction = Direction(0, 1)
        fire_bullet(ai_settings, screen, ship, bullets, direction)
    elif event.key == pygame.K_l:
        direction = Direction(1, 0)
        fire_bullet(ai_settings, screen, ship, bullets, direction)
    elif event.key == pygame.K_j:
        direction = Direction(-1, 0)
        fire_bullet(ai_settings, screen, ship, bullets, direction)
        
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_down = False 

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
                
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
 
def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()
