from player import Player

class Menus():

    def __init__(self):
        print('[INFO] Starting Menu class...')
        player = Player() 
        self.classes = player.get_classes()
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
                    +-+-+----------------------------------------------------+-+-+
        ''')

        while not class_chosen:
            #comment for debug
            # choice = input('> ').lower()
            choice = 'knight'

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
                    '''.format(class_choice, class_stats['attack'], class_stats['defense'], class_stats['strength'], class_stats['skill'], class_stats['intelligence'], class_stats['perception'], class_stats['luck']))
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

        return [ class_choice, char_name ]

    def room_menu(self):
        print('''
                    +-+-+----------------------------------------------------+-+-+
                                          Room Number {}
                    
                                             Menu:
                            "stats": View character stats
                            "inventory": View/Edit character inventory
                            "search": Search the room for loot
                            "move [direction]": Move character to another location
                            "info": Information about the current room
                
                    +-+-+----------------------------------------------------+-+-+
        ''')

        choice = input('> ').lower()

        #TODO: I'd love to replace all of these ifs with some kind of dict based function that works for all of the menus.
        # would do wonders for cleaner code.
        if 'stats' in choice:
            print('this is not ready yet.')
        elif 'inventory' in choice:
            print('this is not ready yet.')
        elif 'search' in choice:
            print('this is not ready yet.')
        elif 'move' in choice:
            print('this is not ready yet.')
        elif 'info' in choice:
            print('this is not ready yet.')

 
    def roll_credits(self):
        raise NotImplementedError

    def check_class_exists(self, class_to_check):
        if class_to_check in self.classes:
            return True
        else:
            print('Hmmm... Are you sure that you chose your class correctly? I am not sure that class exists...')
            return False

