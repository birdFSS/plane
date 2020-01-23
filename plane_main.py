#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pygame

from settings import Settings

def run_game():
	#init game and create a screen object
	pygame.init()
	ai_setting = Settings()
	screen = pygame.display.set_mode(
			(ai_setting.screen_width, ai_setting.screen_height))
	pygame.display.set_caption("Alien Invasion")
	#set color
	bg_color = (230, 230, 230)
	
	# begin to game
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		
		screen.fill(ai_setting.bg_color)
		pygame.display.flip()
		
run_game()


