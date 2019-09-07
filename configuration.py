import yaml
import pathlib

#This file will be used to import characters, maps, actions, etc via YML

def load_character(character_path, character):
    with open(pathlib.Path(character_path)) as file:
        character_configuration = yaml.safe_load(file)
    return character_configuration[character]
