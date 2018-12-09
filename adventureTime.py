ref_dict = {"n": ["north", "forward", "upward"], "s": ["south", "back", "backward"],
            "e": ["east"], "w": ["west"],
            "take": ["take", "grab", "pick"], "items": ["key", "lockpick", "bucket"],
            "look": ["look", "search", "examine"],
            "use": ["use", "interact", "place"]}

class gameManager(object):
        
        def __init__(self):
                print("lol made")

class item(object):
        def __init__(self, name, desc, takable = True, usable_rooms = []):
                self.name = name
                self.desc = desc
                self.takable = takable
                self.usable_rooms = usable_rooms

class room(object):

        def __init__(self, name, desc, links, items = [], locks = []):
                self.name = name
                self.desc = desc
                self.items = items
                self.links = links
                self.locks = locks

class Player(object):

        def __init__(self, cellar):
                print("player made")
                self.current_room = cellar
                self.inv = []
                self.cage_locked = True

item_dict = {}
item_dict["key"] = item("key", "a dull key", True, ["cellar", "entrance_way"])
item_dict["lockpick"] = item("lockpick", "a lockpick. It picks locks", True, ["entrance_way"])
item_dict["bucket"] = item("bucket", "its a bucket. you could put it on your head, but that would't get you far", True, ["fountain"])
item_dict["waterbucket"] = item("waterbucket", "its a bucket. it is filled with water and has some weight to it", True, ["store_cupboard"])
item_dict["cage"] = item("cage", "The cage sits atop a shelf. Nearby there is a balance with a filled bucket dangling from it; making it lean to one side.")
item_dict["note1"] = item("note1", "add some lore")
item_dict["cupboards"] = item("cupboards", "You swing the cupboards open and a spider crawls out onto your arm before quickly disappearing.", False)
item_dict["coats"] = item("coats", "The coats hang from the coat rack and you have a quick shimmy in the pockets to find nothing but some pocket lint and tissues", False)
item_dict["table"] = item("table", "The table is cold. The remnants of food fill your nostrils, but see no signs of a recent dinner anywhere", False)
item_dict["candles"] = item("candles", "The wax is warm to your skin, and the candle was lit recently.", False)

world = {}
world["cellar"] = room("cellar", "A musty old cellar. How come you're down here? The cellar hatch is to the north.", {"N": "kitchen"}, ["duck", "key"], ["N"])
world["kitchen"] = room("kitchen", "An old kitchen, abandoned for years. There are some empty cupboards and a bucket. South is the cellar hatch, north lies a doorway to a room with coats hanging on a rack. East is the dining room.", {"S": "cellar", "E": "dining_room", "N": "coat_racks"}, ["bucket", "cupboards"])
world["dining_room"] = room("dining_room", "A dining room. Candles are burnt out, but fresh. The table lay bare, the eerie silece of the room disturbs you. West is the Kitchen. East is the corridor to outside. ", {"W": "kitchen", "E": "BTECbalcony"})
world["store_cupboard"] = room("store_cupboard", "You see an old key in the corner of the room, locked in a cage.", {"E": "fountain"}, ["cage"])
world["fountain"] = room("fountain", "The crisp wind bites at your skin through your thin clothing. A fountain is in the middle of this small garden", {"W": "store_cupboard", "N": "BTECbalcony"})
world["BTECbalcony"] = room("BTECbalcony", "The room is bare, and seems to serve only to connect the house to the outside world", {"E": "dining_room", "N": "room7", "S": "fountain"})
world["coat_racks"] = room("coat_racks", "The room looks like a welcome room. In the corner there stands a coat rack with some coats on it", {"S": "kitchen", "E": "entrance_way"})
world["entrance_way"] = room("entrance_way", "Entrance way", {"W": "coat_racks"})
world["exit"] = room("exit", "", {})

def show_help():
        print("To traverse the world, use the keyword 'go' along with a specified direction")
        print("Directions are North, east south or west")
        print("")
        print("You can examine the room you are in by simply typing the 'examine' keyword. This gives a description of the room and what you can see")
        print("If you wish to examine a specific item, you can use the 'examine' keyword in conjunction with an item")
        print("")
        print("To pick up items and add them to your inventory, you can use the 'take' keyword in conjunction with an item")
        print("")
        print("You can also use certain items with the 'use' keyword in conjunction with an item")
        print("")
        print("You can view your inventory by typing 'inv'")
        print("")
        print("If you forget what room you are in at any time, simply use the command 'curr'")

def make_list(string):
        
        string = string.lower()
        word_list = string.split(" ")
        if "up" in word_list:
                word_list.remove("up")
        return word_list

def check_locked(direction):
        if direction in player.current_room.locks:
                return True
        else:
                return False

def get_room_desc():
        string = ""
        string = string + player.current_room.desc
        
        for i in range(len(player.current_room.items)):
                if i == 0:
                        string = string + "In the " + player.current_room.name + " you can see a " + player.current_room.items[0]
                else:
                       string = string + " and a " + player.current_room.items[i]
        return string

def use(item):
        if item == "key":
                player.current_room.locks.pop()
                player.inv.remove(item)
                print("The lock opens with an audible click")
        elif item == "bucket":
                player.inv.remove(item)
                player.inv.append("waterbucket")
                world["store_cupboard"].items.append("key")
                print("You fill the bucket with water from the fountain")
        elif item == "waterbucket":
                player.inv.remove(item)
                print("you place the water bucket delicately on the scales, and it balances perfectly; causing the cage door to swing open")

def parse(word_list):
        i = 0
        while i < len(word_list):
                # help check
                if word_list[i] == "help":
                        show_help()
                        break
                
                # look check
                if word_list[i] in ref_dict["look"]:
                        if len(word_list) < i+2:
                                print("\n" + get_room_desc())
                                break
                        else:
                                if word_list[i+1] in item_dict and (word_list[i+1] in player.inv or word_list[i+1] in player.current_room.items):
                                        print(item_dict[word_list[i+1]].desc)
                        break
                
                # movement check
                elif word_list[i] == "go":
                        if word_list[i+1] in ref_dict["n"]:
                                if "N" in player.current_room.links:
                                        if check_locked("N"):
                                                print("The doorway is locked")
                                                break
                                        player.current_room = world[player.current_room.links["N"]]
                                        print("moving to other room")
                        if word_list[i+1] in ref_dict["e"]:
                                if "E" in player.current_room.links:
                                        if check_locked("E"):
                                                print("The doorway is locked")
                                                break
                                        player.current_room = world[player.current_room.links["E"]]
                                        print("moving to other room")
                        if word_list[i+1] in ref_dict["s"]:
                                if "S" in player.current_room.links:
                                        if check_locked("S"):
                                                print("The doorway is locked")
                                                break
                                        player.current_room = world[player.current_room.links["S"]]
                                        print("moving to other room")
                        if word_list[i+1] in ref_dict["w"]:
                                if "W" in player.current_room.links:
                                        if check_locked("W"):
                                                print("The doorway is locked")
                                                break
                                        player.current_room = world[player.current_room.links["W"]]
                                        print("moving to other room")
                        break
                
                # take check
                elif word_list[i] in ref_dict["take"]:
                        print("trying to pick up item")
                        if len(word_list) < i+2:
                                print("please specifiy something to take")
                                break
                        if len(player.current_room.items) > 0:
                                if word_list[i+1] in player.current_room.items:
                                        print("picking up item " + word_list[i+1])
                                        player.inv.append(word_list[i+1])
                                        player.current_room.items.remove(word_list[i+1])
                                else:
                                        print("item not found")
                        break
                
                # use check
                elif word_list[i] in ref_dict["use"]:
                        print("using an item")
                        if len(word_list) < i+2:
                                print("please specify an item to use")
                                break
                        if word_list[i+1] in player.inv and item_dict[word_list[i+1]].takable == True: #or word_list[i+1] in player.current_room.items:
                                print("using item " + word_list[i+1])
                                use(word_list[i+1])
                        else:
                                print("item not in inventory")

                        break
						
		# test checks converted to player-usable commands
                elif word_list[i] == "curr":
                        print(player.current_room.name)
                        break
                elif word_list[i] == "inv":
                        print(player.inv)
                        break
                else:
                        break
        i += 1
        print("")

gameRunning = True
player = Player(world["cellar"])
print("At anytime during the game, you can type 'help' for a list of known commands.")
print("Here is a list now:")
show_help()
input("Press [ENTER] to start your adventure!")
print("You wake up in a cold, dingy room. Your skin is covered in filth and you smell")
print("The dirt you lie on is wet and insect-ridden.")
print("You see a crack of light above you (north)")
while(gameRunning):
        playerInput = input("What do you do?")
        parse(make_list(playerInput))









