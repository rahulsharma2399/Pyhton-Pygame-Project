import sys #to exit the game

import pygame
import game_function as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    ai_settings=Settings() #attribute as a instance
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alian_invasion")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    ship=Ship(ai_settings,screen)
    bullets=Group() #we make Group of those instances which are move without key or mouse interuption. i.e we dont make group of ship bcz it will be moved by the player
    aliens = Group()
    
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen,ship, aliens)
    stats=GameStats(ai_settings)
    sb= Scoreboard(ai_settings, screen, stats)
    while True:
        gf.check_events(ai_settings, screen,stats,sb,play_button ,ship,aliens, bullets)
    
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship, aliens,bullets)
        gf.update_screen(ai_settings, screen,stats,sb,ship, aliens, bullets,play_button)
        
run_game()
