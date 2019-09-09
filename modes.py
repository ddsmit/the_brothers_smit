import arcade

#This file will contain the logic for the different game types.

class Mode(arcade.Window):
    def __init__(self):
        self.characters = None
        self.map = None
    def initiate(self, characters, map):
        self.characters = characters
        self.map = map
        self.build_characters()
        self.build_map()
        self.start()

    def build_characters(self):
        pass

    def build_map(self):
        pass

    def start(self):
        pass

class MainMenu(Mode):
    pass

class BattleMode(Mode):
    def start(self):
        self.determine_turns()
        self.turn(self.turns)

    def determine_turns(self):
        #cycle through characters and determine step order
        self.turns = None

    def turn(self):
        pass

    def next_turn(self):
        self.turn_index += 1



class ExploreMode(Mode):
    pass