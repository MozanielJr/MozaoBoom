import pygame
import sys

def check_events(ship):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_rigth = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
    
                    

                    
def update_screen(mb_settings, screen, ship):
   	
    screen.fill(mb_settings.bg_color)
    ship.blitme()		
    pygame.display.flip()



