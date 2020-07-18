import json
from utils import log

class Player():

    def __init__(self):
        log('[[INFO] Player.__init__] Init Player class', 1)
        self.player_config = {}
        self.player_inventory = {}
        with open('config/class_configs.json') as classes:
            self.avail_classes = json.load(classes)['classes']
            log('[[INFO] Player.__init__] Successfully loaded class_configs.json', 1)

    
    def create_character(self, name, char_class):

        if not name:
            log('[[WARN] Player.create_character] No player name supplied. Cannot create character.', 2)
            return False

        if not char_class:
            log('[[WARN] Player.create_character] No player class supplied. Cannot create character.', 2)
            return False 

        if char_class in self.avail_classes:
            self.player_config.update({
                'stats': self.avail_classes[char_class],
                'class': char_class,
                'name': name
            })
            self.player_inventory.update(self.avail_classes[char_class]['inventory'])
            self.update_character_config()
            log('[[INFO] Player.create_character] Successfully created character {0} under the {1} class.'.format(name, char_class), 1)
        else:
            log('[[WARN] Player.create_character] Invalid character class supplied. Please supply a valid character class.', 2)
            return False

    def get_classes(self):
        return self.avail_classes
    
    #hmmmmm.....
    def update_character_config(self):
        updated_player_info = self.player_config
        updated_player_info.update({
            "inventory": self.player_inventory
        })
        with open('config/player_config.json', 'w') as player:
            json.dump(updated_player_info, player)

        return{
            "leave": False
        }

    def get_current_player(self):
        return self.player_config
    
    def get_player_inventory(self):
        return self.player_config

