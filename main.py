import pygame
import sys
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
	pygame.init()
	mb_settings = Settings()
	screen = pygame.display.set_mode((mb_settings.screen_width,mb_settings.screen_heigth))
	pygame.display.set_caption("Mozão Boom")
	ship = Ship(screen)
    
	while True:

		gf.check_events(ship)
		ship.update()
		gf.update_screen(mb_settings,screen,ship)		
		
run_game()