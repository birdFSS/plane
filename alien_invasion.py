#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pygame

from ship import Ship
from settings import Settings
import game_functions as gf

def run_game():
    #init game and create a screen object
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode(
            (ai_setting.screen_width, ai_setting.screen_height))
    
    pygame.display.set_caption("Alien Invasion")
    
    ship = Ship(screen)
    
    # begin to game
    while True:
        gf.check_events()
        
        screen.fill(ai_setting.bg_color)
        ship.blitme()
        
        pygame.display.flip()
        
run_game()


