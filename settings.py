
class Settings:
    """Class to control the general settings"""
    def __init__(self):

        # Screen config (16:9 para bater certo com os backgrounds)
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (20, 15, 30)
        self.screen_caption = "Olympus Devour by Rodrigo Aguiar"

        # Main caracter configs
        self.mc_speed = 5
        self.mc_scale = 2.5  # Multiplies the original size of the sprite (adjust between 2 and 3)
