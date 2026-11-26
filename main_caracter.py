import pygame

class Main_caracter:
    """Class to control the main caracter details"""

    def __init__(self, od_game):

        self.screen = od_game.screen
        self.screen_rect =  od_game.screen.get_rect()
        self.settings = od_game.settings

        #Flag of movement control
        self.moving_right = False
        self.moving_left = False

        # Load the main caracter image and get its rect
        self.image = pygame.image.load('images/male_maincaracter.png')

        # Load the main caracter image and scale it
        raw_image = pygame.image.load('images/male_maincaracter.png').convert_alpha()
        new_width = int(raw_image.get_width() * self.settings.mc_scale)
        new_height = int(raw_image.get_height() * self.settings.mc_scale)
        self.image = pygame.transform.scale(raw_image, (new_width, new_height))

        self.rect = self.image.get_rect()
        # Starts the main caracter at the mid bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Updates the position of the caracter on base of the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.mc_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
                    self.x -= self.settings.mc_speed

        #Update rect obj from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the main caracter at its current location."""
        self.screen.blit(self.image, self.rect)