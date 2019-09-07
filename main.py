import arcade
import os
import modes

#This file will be the first one that runs that contains the start menu
#and any other menus that are needed. This file will also cordinate
#between the different modes

class GameInitialize(arcade.Window):
    def __init__(self):
        super().__init__(screen_width, screen_height, screen_titel)
        self.file_path = os.path.dirname(os.path.abspath(__file__))
        self.game_mode = self.main_menu

    def start_game(self):
        self.frame_count = 0
        self.all_sprites_list = arcade.SpriteList()
        self.map_sprites_list = arcade.SpriteList()
        self.character_sprites_list = arcade.SpriteList()
        self.misc_sprites_list = arcade.SpriteList()

        self.build_characters()
        self.build_map()

    def build_characters(self):
        pass

    def build_map(self):
        pass

    def on_draw(self):
        arcade.start_render()

def main():
    window = MyGam