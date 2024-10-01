current_room = "entrance"
inventory = []
locked_rooms = ["secret room", "armory", "the grand hall", "throne room", "the escape tunnel"]
#----------------------------------------------------------------------------------
# This dict represents all the rooms in castle with there descriptions and 
# the objects they contains
rooms = {
    "entrance": {
        "description": "You are at the entrance of a castle, with three routes and a chest containing a paper and a hammer.",
        "items": ['the paper in chest', 'hammer'],
        "exits": {"south": "the grand hall", "west": "library", "east": "dungeon"},
    },
    "library": {
        "description": "In the library, you find a seceret door.",
        "items": ["the strange book", "piece of cloth"],
        "exits": {"east": "entrance", "south": "secret room"},
    },
    "secret room": {
        "description": "You are in a secret room with a closet holding a key, locked by an old rusty lock.",
        "items": ["the sword key"],
        "exits": {"north": "library"},
    },
    "dungeon": {
        "description": "You entered the dungeon, but a door puzzle challenges you.",
        "items": [],
        "exits": {"west": "entrance", "south": "armory"},
    },
    "armory": {
        "description": "You are in the armory, surrounded by weapons and armor, with a sword and knife on a shelf.",
        "items": ["sword", "knife"],
        "exits": {"north": "dungeon"},
    },
    "the grand hall": {
        "description": "You are in the grand hall, where a huge door leads to the throne room.",
        "items": [],
        "exits": {"north": "entrance", "south": "throne room"},
    },
    "throne room": {
        "description": "You stand in the throne room, where a passage leads to an escape tunnel.",
        "items": [],
        "exits": {"north": "the grand hall", "south": "the escape tunnel"},
    },
    "the escape tunnel": {
        "description": "You have finally escaped the castle!",
        "items": [],
        "exits": {},
    }
}
#-------------------------------------------------------------------------

def puzzle_game1():
    check = True
   
    print("To unlock the door, you must solve this riddle:")
    riddle ='''
        I speak without a mouth and hear without ears. 
        I have no body, but I come alive with the wind. 
        What am I?
        '''
    print(riddle)
    while check:
        answer = input("Your answer: ").lower()
        if answer == "echo":
            print("Correct! The door unlocks with a soft click.")
            return True
        else:
            print("Wrong answer! Try again.")
    

#-------------------------------------------------------------------------

def puzzle_game2():
    check = True
    print("To proceed, solve this puzzle:")
    puzzle = '''
    Arrange the numbers in ascending order:
    2 3 1 4 8 7 6 5
    '''
    while check:
        print(puzzle)
        answer = input("Your answer: ")
        if answer == "1 2 3 4 5 6 7 8":
            print("Correct! The door unlocks with a soft click.")
            return True
        else:
            print("Wrong answer! Try again.")


#-------------------------------------------------------------------------

def instructions():
    print('''
          Commands:
          look - To look at the current room description
          go [direction] - Move to a specific room
          take [item] - To pick an item and add to inventory
          drop [item] - To drop and item from inventory
          use [item] - Use an item in the current room
          examine [object] - Get more details about an object
          show inventory - Display the items in your inventory
          save - Save your game progress
          load - Load a saved game
          quit - Exit the game
          help - Display available commands
          ''')
    
#-------------------------------------------------------------------------

def look(current_room):
    if current_room in rooms:
        print(rooms[current_room]['description'])
        print(f"The exits are: {rooms[current_room]['exits']}")
        if rooms[current_room]["items"] is not None:
            print(f"There are {rooms[current_room]['items']}")


#--------------------------------------------------------------------------------------------------
#       Move from one room to other
def move_player(direction):
    global current_room
    
    if direction not in rooms[current_room]['exits']:
        print(f"You cannot go {direction} from here!")
        return
    
    next_room = rooms[current_room]['exits'][direction]
    
    if next_room in locked_rooms:
        
        print("The door is locked!")
        
        if next_room == "throne room":
            print(
                '''
                As you tried to open the door, the door was locked and 
                there was a puzzle game popped out of a wall.
                ''')
            won = puzzle_game1()
            if won:
                print("The door is unlocked!")
                current_room = next_room
                locked_rooms.remove("throne room")
                print("You have entered the throne room!")
                look(current_room)
            return
        if next_room == "armory":
            print(
                '''
                As you tried to open the door, the door was locked and 
                there was a puzzle game popped out of a wall.
                ''')
            won = puzzle_game2()
            if won:
                print("The door is unlocked!")
                current_room = next_room
                locked_rooms.remove("armory")
                print("You have entered the Armory!")
                look(current_room)
            return 
         
        if next_room == "the grand hall":
           print("You need a key to open the door!")
           return
        if next_room == "the escape tunnel":
            print("You need a sword to open the door!")
            return
        if next_room == "secret room":
            print("You need a passcode to open the door!")
            return
    else:   
        current_room = next_room
        return


#--------------------------------------------------------------------------------------------------
def use_item(item):
    if item in inventory:
        if item == "the sword key" and current_room == "entrance":
            print(
                '''
                The sword key unlocks the door, and it creaks open slowly.
                ''')
            inventory.remove(item)
            rooms[current_room]["items"].append(item)
            locked_rooms.remove("the grand hall")
            move_player("south")
            
            
        elif item == "sword" and current_room == "throne room":
            print(
                '''
                You place the sword in the slot, revealing a hidden passage to escape.
                ''')
            inventory.remove(item)
            rooms[current_room]["items"].append(item)
            locked_rooms.remove("the escape tunnel")
            move_player("south")
            
        elif item == "the paper in chest" and current_room == "library":
            print(
                '''
                The passcode works! A secret door behind the bookshelf opens.
                '''
            )
            inventory.remove(item)
            rooms[current_room]["items"].append(item)
            locked_rooms.remove("secret room")
            move_player("south")


#-------------------------------------------------------------------------
def take_item(item):
    if item in rooms[current_room]["items"]:
        inventory.append(item)
        print(f"{item} added to the inventory!")
    else:
        print("There is no such item found in room!")
        
    rooms[current_room]["items"].remove(item)
        
#-------------------------------------------------------------------------

def drop_item(item):
    if item in inventory:
        inventory.remove(item)
        rooms[current_room]["items"].append(item)
        print(f"{item} dropped!")
    else:
        print("The inventory does not contain such item!")


#-------------------------------------------------------------------------

def examine_object(object):
    
    if object == "the sword key":
        print("The key is beautifully embellished with intricate designs, and it has a sword sign on it.")
    elif object == "sword":
        print("The sword is a long, gleaming blade with a sharp edge and a jeweled hilt.")
    elif object == "the paper in chest":
        print("The paper is old and yellowed, with four digit number on it: 1234.")
        
#-------------------------------------------------------------------------

def show_inventory():
    if len(inventory) == 0:
        print("The inventory is empty!")
        return
    
    print("Inventory:")
    for item in inventory:
        print(item)

#-------------------------------------------------------------------------

def save_game():
    pass    
#-------------------------------------------------------------------------

def load_game():
    pass

#-------------------------------------------------------------------------

def main():
    print("======Welcome to the Mysterious Castle Adventure!======")
    instructions()
    
    while True:
        command = input("What would you like to do? ").lower().strip()
        
        if command == "quit":
            print("Thanks for playing!")
            break
        
        elif command == "look":
            look(current_room)
            
        elif command.startswith("go "):
            move_player(command[3:])
                
        elif command.startswith("take "):
            take_item(command[5:])
                
        elif command.startswith("drop "):
            drop_item(command[5:])
            
        elif command.startswith("use "):
            use_item(command[4:])
        
        elif command == "show inventory":
            show_inventory(command)
        
        elif command.startswith("examine "):
            examine_object(command[8:])
        
        elif command == "save":
            save_game()
        
        elif command == "load":
            load_game()
        
        elif command == "help":
            instructions()
            
if __name__ == "__main__":
    main()