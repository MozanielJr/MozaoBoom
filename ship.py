import pygame

class Ship:

    def __init__(self, screen):

        self.screen = screen
        self.image = pygame.image.load('images/ship.png')
        self.image_size = (70,70)
        self.image = pygame.transform.scale(self.image, self.image_size)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_rigth = False
        self.moving_left = False


    def update(self):
        if self.moving_rigth and self.rect.right < self.screen_rect.right:
            self.rect.centerx +=1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -=1
    
    def blitme(self):

        self.screen.blit(self.image, self.rect)