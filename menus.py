from player import Player
from game import Game
from utils import log

class Menus():

    def __init__(self):
        log('[[INFO] Menus.__init__] Init Menus class', 1)
        self.player = Player()
        self.classes = self.player.get_classes()
        print('''
        :::::::::  :::::::::: ::::    ::: ::::    ::: ::::::::::: :::::::::: ::::::::                          
        :+:    :+: :+:        :+:+:   :+: :+:+:   :+:     :+:     :+:       :+:    :+:                         
        +:+    +:+ +:+        :+:+:+  +:+ :+:+:+  +:+     +:+     +:+       +:+                                
        +#++:++#+  +#++:++#   +#+ +:+ +#+ +#+ +:+ +#+     +#+     +#++:++#  +#++:++#++                         
        +#+        +#+        +#+  +#+#+# +#+  +#+#+#     +#+     +#+              +#+                         
        #+#        #+#        #+#   #+#+# #+#   #+#+#     #+#     #+#       #+#    #+#                         
        ###        ########## ###    #### ###    #### ########### ########## ########                          
            :::     :::::::::  :::     ::: :::::::::: ::::    ::: ::::::::::: :::    ::: :::::::::  :::::::::: 
          :+: :+:   :+:    :+: :+:     :+: :+:        :+:+:   :+:     :+:     :+:    :+: :+:    :+: :+:        
         +:+   +:+  +:+    +:+ +:+     +:+ +:+        :+:+:+  +:+     +:+     +:+    +:+ +:+    +:+ +:+        
        +#++:++#++: +#+    +:+ +#+     +:+ +#++:++#   +#+ +:+ +#+     +#+     +#+    +:+ +#++:++#:  +#++:++#   
        +#+     +#+ +#+    +#+  +#+   +#+  +#+        +#+  +#+#+#     +#+     +#+    +#+ +#+    +#+ +#+        
        #+#     #+# #+#    #+#   #+#+#+#   #+#        #+#   #+#+#     #+#     #+#    #+# #+#    #+# #+#        
        ###     ### #########      ###     ########## ###    ####     ###      ########  ###    ### ########## 
                                            Version 0.1
                                    Made with love, from Brennan
                    +-+-+----------------------------------------------------+-+-+
                                            Main Menu

                                    "play": Start the game
                                    "credits": Roll the credits
                                    "quit": Quit to terminal
                    +-+-+----------------------------------------------------+-+-+
        ''')
    
    def main_menu(self):
        #comment out for debug
        # choice = input('> ').lower()
        choice = 'play'

        log('[[INFO] Menus.main_menu] User choice was: {0}'.format(choice), 1)

        if 'play' in choice:
            return True
        elif 'credits' in choice:
            self.roll_credits()
        elif 'quit' in choice:
            exit()
        else:
            self.main_menu()
    
    def class_menu(self):
        class_chosen = False
        classes = self.classes

        print('''
                    +-+-+----------------------------------------------------+-+-+
                                        Choose a class:

                                            Options:
                                "[classname]": Pick class
                                "info [classname]": Class details

                                            Classes:
                                "Knight": Strong, balanced character
                                "Custom": Create a custom class
                    +-+-+----------------------------------------------------+-+-+
        ''')

        while not class_chosen:
            #comment for debug
            # choice = input('> ').lower()
            choice = 'knight'

            log('[[INFO] Menus.class_menu] User choice was: {0}'.format(choice), 1)

            if 'info' in choice:
                class_choice = choice.split(' ')[1]

                if self.check_class_exists(class_choice):
                    class_stats = classes[class_choice]

                    print('''
                    +-+-+----------------------------------------------------+-+-+
                                            Class Name:
                                                {}

                                            Stats:
                                        "attack": {}
                                        "defense": {}
                                        "strength": {}
                                        "skill": {}
                                        "perception": {}
                                        "intelligence": {}
                                        "luck": {}
                    +-+-+----------------------------------------------------+-+-+
                    '''.format(class_choice, class_stats['attack'], class_stats['defense'],
                    class_stats['strength'], class_stats['skill'], class_stats['intelligence'],
                    class_stats['perception'], class_stats['luck']))
            else:
                if self.check_class_exists(choice):
                    class_choice = choice
                    class_chosen = True
            
        print('''
                    +-+-+----------------------------------------------------+-+-+
                                What will your characters name be?
                    +-+-+----------------------------------------------------+-+-+
        ''')
        #comment out for debug
        # char_name = input('> ')
        char_name = "test_character"

        log('[[INFO] Menus.main_menu] Character name is: {0}'.format(char_name), 1)

        return [ class_choice, char_name ]

    def room_menu(self, room):
        print('''
                    +-+-+----------------------------------------------------+-+-+
                                          Room Number {}
                    
                                             Menu:
                            "stats": View character stats
                            "inventory": View/Edit character inventory
                            "search": Search the room for loot
                            "move [direction]": Move character to another location
                            "info": Information about the current room
                            "save": Save your current character
                
                    +-+-+----------------------------------------------------+-+-+
        '''.format(room['number']))
        choice = input('> ').lower()
        log('[[INFO] Menus.room_menu] User choice was: {0}'.format(choice), 1)

        #TODO: I'd love to replace all of these ifs with some kind of dict based function that works for all of the menus.
        # would do wonders for cleaner code.
        return choice

 
    def roll_credits(self):
        log('[[CRITICAL] Menus.roll_credits] roll_credits does not yet exist.', 4)
        raise NotImplementedError

    #TODO: This would be dope.
    def generate_custom_class(self):
        log('[[CRITICAL] Menus.roll_credits] generate_custom_class does not yet exist.', 4)
        raise NotImplementedError

    def display_stats(self, current_stats):
        print('''
                    +-+-+----------------------------------------------------+-+-+
                                            Stats:
                                        "attack": {}
                                        "defense": {}
                                        "strength": {}
                                        "skill": {}
                                        "perception": {}
                                        "intelligence": {}
                                        "luck": {}
                    +-+-+----------------------------------------------------+-+-+
                    '''.format(current_stats['attack'], current_stats['defense'],
                    current_stats['strength'], current_stats['skill'], current_stats['intelligence'],
                    current_stats['perception'], current_stats['luck']))
        
        #this seems dumb right now but it's smart I swear.
        #oh god why was this smart I don't remember.
        return {
            'leave': False
        }
    
    def manage_inventory(self):
        print('''
        
                    +-+-+----------------------------------------------------+-+-+
                                Inventory Menu:
                                        "Weapons"
                                        "Armor"
                                        "Consumables"
                                        "Rings"
                                        "Misc"
                                        "Exit"
                    +-+-+----------------------------------------------------+-+-+
        ''')

        leave_inventory = False
        while not leave_inventory:

            choice = input('> ').lower()

            log('[[INFO] Menus.manage_inventory] User choice was: {0}'.format(choice), 1)

            if choice not in "exit":
                self.inventory_drilldown(choice)
            else:
                leave_inventory = True
            
    def inventory_drilldown(self, choice):
        print('hi')

    def check_class_exists(self, class_to_check):
        if class_to_check in self.classes:
            return True
        else:
            log('[[WARN] Menus.check_class_exists] {0} is not an operable player class name.'.format(class_to_check), 2)
            return False

