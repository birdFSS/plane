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
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invasion")
    
    ship = Ship(ai_settings, screen)
    
    # begin to game
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        
        
run_game()


