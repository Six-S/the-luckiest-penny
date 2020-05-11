import random
import json

class Game():

    def __init__(self):
        print('Starting Game class.....')
        self.turn_num = 0
        self.room_num = 0
        #these won't change during the course of the game, so we're safe to load it in on init.
        with open('config/item_config.json') as items:
            self.item_config = json.load(items)
        with open('config/config.json') as config:
            config = json.load(config)
            self.enemy_config = config['enemy_config']
            self.room_config = config['room_config']


    def should_spawn_bad_guy(self, current_stats):
        #this may be dumb, but for right now I'm just gonna establish something to keep moving.
        #This function takes player luck into account.
        bad_guy = {}

        enemy_diff_config = self.enemy_config['enemy_difficulty']
        enemy_item_drop_config = self.enemy_config['enemy_item_drop']
        enemy_weapon_drop_config = self.enemy_config['enemy_drops_weapon']
        enemy_type = self.enemy_config['enemy_type']

        enemy_diff_num = self.chance(100) - current_stats['luck']
        enemy_should_drop_item_num = self.chance(100) + current_stats['luck']
        enemy_should_drop_weapon_num = self.chance(100) + current_stats['luck']
        enemy_type_num = self.chance(100)


        bad_guy['strength'] = self.returnConfigValue(enemy_diff_num, enemy_diff_config)
        bad_guy['item_dropped'] = self.returnConfigValue(enemy_should_drop_item_num, enemy_item_drop_config)
        bad_guy['weapon_dropped'] = self.returnConfigValue(enemy_should_drop_weapon_num, enemy_weapon_drop_config)
        bad_guy['type'] = self.returnConfigValue(enemy_type_num, enemy_type)

        return bad_guy
    
    def room_configuration(self, current_stats):

        room = {}

        room_hazard_num = self.chance(100) - current_stats['luck']
        room_item_drop_num = self.chance(100) + current_stats['luck']

        room['hazard'] = self.returnConfigValue(room_hazard_num, self.room_config['hazards'])
        room['item_drop'] = self.returnConfigValue(room_item_drop_num, self.room_config['item_drop'])
        room['number'] = self.room_num

        return room

    def increment_turn_num(self):
        self.turn_num = self.turn_num + 1
        return self.turn_num
    
    def increment_room_num(self):
        self.room_num = self.room_num + 1
        return self.room_num

    def chance(self, max):
        return random.randint(1, max)
    
    #Checks the randomly generated number against the config passed in
    def returnConfigValue(self, num, config):
        #Hmmm this is kinda trash.
        for key, value in config.items():
            if num <= value:
                return key
