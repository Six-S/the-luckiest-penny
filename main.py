from player import Player
from menus import Menus
from game import Game

if __name__ in '__main__':

    #run main menu
    levelOver = False
    menu = Menus()
    game = Game()

    menu.main_menu()

    #start by creating our character.
    class_choice = menu.class_menu()

    #If we're here, we'll create an instance of our player class
    character_class = Player()
    character_class.create_character(class_choice[1], class_choice[0])

    print(character_class.get_current_player())

    #some story intro of some kind will go here.
    #We gotta introduce what we're doing and why.

    #Now we're past the intro.
    #"You enter the valley, not sure what will come next, etc. etc."

    room_menu_choices = { 
        'stats': menu.display_stats,
        'inventory': menu.manage_inventory,
        'search': None,
        'move': None,
        'info': None,
        'save': character_class.update_character_config,
        'attack': None,
        'defend': None,
        'dodge': None
    }

    stat_changes = {
        'damage': None
    }

    #Eh, while loop. There's a better way to do this, I'm sure.
    while not levelOver:

        #we're starting a new turn, so increment as such.
        game.increment_turn_num()
        game.increment_room_num()

        #Start by generating some numbers, we need to figure out what will take place in this room.
        current_stats = character_class.get_current_player()['stats']

        #generate enemy details
        enemy = game.should_spawn_bad_guy(current_stats)
        print(enemy)

        room = game.room_configuration(current_stats)
        print(room)

        in_room = True
        while in_room:
            choice = menu.room_menu(room)

            if choice in room_menu_choices:
                #trash var name, but this stores changes that happened because of the players choice.
                #Must be dict
                effect = room_menu_choices[choice](current_stats)
            else:
                print('Invalid selection, please try again.')

            if effect['leave']:
                in_room = False

        #we quit out for right now, we testin'.
        levelOver = True

