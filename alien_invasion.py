import sys
import pygame
from settings import Settings
from ship import SimbaShip
from bullet import Bullet
from time import sleep
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class RyanInvasion:
    """overall class to manage game assets and behavior"""
    def __init__(self):
        """initialize the game and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.gamestats = GameStats()
        self.screen =  pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Ryan Invasion")
        self.ship = SimbaShip(self)
        self.playbutton = Button(self, "Play")
        # background image
        self.background =  pygame.image.load(self.settings.background_image)
        # bullets + aliens
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self._check_bottom_screen()
        self.game_active = False
        self.playbuttonactive = True
        self.sb = Scoreboard(self)
        self.highscorefile = 'highscore.txt'
    def _create_alien(self, x_position, y_position):
        """create alien and place in row"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.y = y_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
    def _create_fleet(self):
        """creating fleet of ryans"""
        # make an alien
        alien = Alien(self)
        self.aliens.add(alien)
        # create an alien and keep adding them until there is no more room
        alien_width, alien_height = alien.rect.width, alien.rect.height
        current_x, current_y = alien_width, alien_height
        screen_width, screen_height = self.settings.screen_width, self.settings.screen_height
        alien_dist = self.settings.alien_amt 
        # add aliens horizontally + vertically
        while current_y < (screen_height - alien_dist * alien_height):
            while current_x < (screen_width-1*alien_width):
                self._create_alien(current_x, current_y)
                current_x += 1.5* alien_width
            # after row done, reset x + increment y
            current_x = alien_width
            current_y += 1.5*alien_height
    def _move_aliens(self):
        for alien in self.aliens:
            movement = self.settings.alien_speed
            direction = self.settings.alien_direction
            alien.rect.x += direction*movement #alien moves at speed in direction
            if alien.rect.x >= 1100 or alien.rect.x <= 40:
                self._drop_alien()
                for alien in self.aliens:
                    self.settings.alien_direction *= -1
                    break
    def _drop_alien(self):
        for alien in self.aliens:
            alien.rect.y += self.settings.alien_y_drop 
    def _fire_bullet(self):
            """make new bullet and add it to the bullets group"""
            if len(self.bullets)<self.settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)
    def _check_old_bullets(self):
        """get rid of bullets that have disappeared"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    def _update_bullets(self):
        """detect if a bullet hits an alien"""
        """if so, remove bullet and alien"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.gamestats.score += 100
                self.sb.prep_score()
                self.check_high_score()
            self.check_high_score()
    def check_high_score(self):
        """check for new high score"""
        highscorefile = self.highscorefile
        if self.gamestats.score >= self.gamestats.high_score:
            self.gamestats.high_score = self.gamestats.score
            self.sb.prep_high_score() 
            with open(highscorefile, 'w') as file:
                file.write(str(self.gamestats.score))

        
    def _level_up(self):
        if self.aliens.sprites():
            pass
        else:
            self.gamestats.level += 1
            print(f"Level{self.gamestats.level}")
            # increase difficulty
            self.settings.ship_speed += 0.2
            self.settings.bullet_speed += 0.1
            self.settings.alien_y_drop += 0.5
            self.settings.alien_speed += 0.2
            sleep(0.5)
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()

    def _check_bottom_screen(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                """Treat this the same as if the ship got hit"""
                self.ship_hit()
                break
    def _ship_hit(self):
        """kills game once the ship is hit by an alien ship"""
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            if self.gamestats.lives_left > 0:
                # remove a life
                self.gamestats.lives_left -= 1
                # get rid of aliens and bullets
                self.bullets.empty()
                self.aliens.empty()
                self._create_fleet()
                self.ship.center_ship()
                # pause for a sec
                sleep(1)
            else:
                self.game_active = False
                print("Game over")
                
    def _update_screen(self):
        # make the most recently drawn screen visible
            self.screen.blit(self.background,(0,0))
            self.ship.blitme()
            self._level_up()
            self._move_aliens()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.clock.tick(60)
            self._ship_hit()
            if self.gamestats.game_active:
                self.aliens.draw(self.screen)
                self._move_aliens()
                self._check_old_bullets()
                self.ship.update()
                self.bullets.update()
                self._update_bullets()
            if self.playbuttonactive:
                self.playbutton.draw_button()
            self.sb.show_score()
            pygame.display.flip()   
    def _keybrd_mouse_events(self):
        """watches for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)
            if self.gamestats.game_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                    elif event.key == pygame.K_SPACE:
                        self._fire_bullet()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
            
    def check_play_button(self, mouse_position):
        """start a new game when pllayer clicks play"""
        button_clicked = self.playbutton.rect.collidepoint(mouse_position)
        if button_clicked and not self.gamestats.game_active:
            self.playbuttonactive = False
            self.settings.initialize_dynamic_settings()
            self.sb.prep_score()
            sleep(0.3)
            self.gamestats.game_active = True
            self.bullets.empty()
    def run_game(self):
        """start the main loop for the game"""
        while True:
            self._keybrd_mouse_events()
            self._update_screen()
if __name__ == '__main__':
    # make a game instance and run the game
    ri = RyanInvasion()
    ri.run_game()


