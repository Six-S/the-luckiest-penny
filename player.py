import json


class Player():

    def __init__(self):
        print('Starting character class....')
        self.player_config = {}
        self.player_inventory = {}
        with open('config/class_configs.json') as classes:
            self.avail_classes = json.load(classes)['classes']

    
    def create_character(self, name, char_class):

        if not name:
            print('Must include name to create a new character.')
            return False

        if not char_class:
            print('Must include a character class type to create a new character.')
            return False 

        if char_class in self.avail_classes:
            self.player_config.update({
                'stats': self.avail_classes[char_class],
                'class': char_class,
                'name': name
            })
            self.player_inventory.update(self.avail_classes[char_class]['inventory'])
            self.update_character_config()
        else:
            print('Must include a valid character class type to create a new character.')
            return False

    def get_classes(self):
        return self.avail_classes
    
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
        print(':thinking:', self.player_config)
        return self.player_config
    
    def get_player_inventory(self):
        return self.player_config

