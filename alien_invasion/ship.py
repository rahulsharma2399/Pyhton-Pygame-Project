import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen=screen

        self.image=pygame.image.load("C:/Users/VAIO/Desktop/ship.bmp")
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.ai_settings = ai_settings #to have control on ship setting


        self.rect.centerx=self.screen_rect.centerx  
        self.rect.bottom=self.screen_rect.bottom

        self.center = float(self.rect.centerx) #bcz we increse centerx by 1.5 so it should be indecimal
        
        #movement flag
        self.moving_right = False
        self.moving_left = False

        
        
    def update(self):
        """update the ship's movement based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:   #use of after and== to stop ship to go outside the screen
            self.center +=self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -=self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image,self.rect)


    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx    

 
        
