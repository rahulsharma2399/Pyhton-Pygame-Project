import pygame
from pygame.sprite import Sprite

"""we import from the
pygame.sprite module. When you use sprites, you can group related elements
in your game and act on all the grouped elements at once."""

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
# Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
# Store the alien's exact position.
        self.x = float(self.rect.x)
    def blitme(self):

        self.screen.blit(self.image, self.rect)


    def update(self):

        """Move the alien right."""
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor *self.ai_settings.fleet_direction)
        
        self.rect.x = self.x


    def check_edges(self):

        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
