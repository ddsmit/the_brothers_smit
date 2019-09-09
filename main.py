import arcade
import os
import modes

#This file will be the first one that runs that contains the start menu
#and any other menus that are needed. This file will also cordinate
#between the different modes

class Game(arcade.Window):
    def __init__(self):
        super().__init__(screen_width, screen_height, screen_title)
        self.file_path = os.path.dirname(os.path.abspath(__file__))
        self.game_mode = modes.MainMenu()
        self.game_mode.initiate()

    def on_draw(self):
        arcade.start_render()


def main():
    window = Game()
    window.start_game()
    arcade.run()


if __name__ == "__main__":
    main()