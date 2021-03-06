ref_dict = {"n": ["north", "forward", "upward"], "s": ["south", "back", "backward"],
            "e": ["east", "left"], "w": ["west", "right"],
            "take": ["take", "grab", "pick"], "drop": ["drop", "throw"],
            "look": ["look", "search", "examine"],
            "use": ["use", "interact", "place"]}

class item(object):
        def __init__(self, name, desc, takable = False, usable_rooms = []):
                self.name = name
                self.desc = desc
                if takable == "True" or takable == "true":
                    self.takable = True
                else:
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
                #print("player made")
                self.current_room = cellar
                self.inv = []
                self.cage_locked = True

def make_item_dict():
        #open file in read mode and get array of lines
        try:
                file = open("items.txt", "r")
                linearray = file.readlines()
        except:
                raise Exception("Could not open item index file. Is items.txt present in this folder?")
        for i in range(len(linearray)):
                # skip first line
                if i == 0:
                        pass
                else:
                        # split on commas
                        tempitem = linearray[i].split(";")
                        #print(tempitem)
                        # make item
                        #print(len(tempitem))
                        # different cases for items since there are optional parameters, so dont want to go over the array length
                        if len(tempitem) == 3: # no optional paramters given
                                item_dict[tempitem[0]] = item(tempitem[1], tempitem[2])
                        elif len(tempitem) == 4: # takable optional parameter taken
                                item_dict[tempitem[0]] = item(tempitem[1], tempitem[2], tempitem[3], [])
                        elif len(tempitem) == 5: # above and usable rooms optional paramters taken
                                # make list for usable room from string, so that i pass a list into the item class (userooms), not a string
                                # since we can not search through a string like a list to check rooms
                                # delete brackets
                                tempitem[4] = tempitem[4][1:len(tempitem[4])-2]
                                # split on comma
                                userooms = tempitem[4].split(",")
                                item_dict[tempitem[0]] = item(tempitem[1], tempitem[2], tempitem[3], userooms)
        #print("item dictionary made")

item_dict = {}

make_item_dict()

# items added to the item text file have been hashed out

#Cellar items

#item_dict["key"] = item("key", "a dull key", True, ["cellar", "entrance_way"])
#item_dict["duck"] = item("duck", "a squeaky duck", True)
#item_dict["dirt"] = item("dirt", "Moist ground that squelches under the pressure of your bare foot")

#Kitchen items

#item_dict["bucket"] = item("bucket", "its a bucket. you could put it on your head, but that would't get you far.", True, ["fountain"])
#item_dict["cupboards"] = item("cupboards", "You swing the cupboards open and a spider crawls out onto your arm before quickly disappearing.")
#item_dict["oven"] = item("oven", "The oven is off; cold.")
#item_dict["knife"] = item("knife", "The knife has a distinctively dull blade.", True)

#Coats items

#item_dict["coats"] = item("coats", "The coats hang from the coat rack and you have a quick shimmy in the pockets to find nothing but some pocket lint and tissues.")
#item_dict["coatrack"] = item("coatrack", "The coatrack is made of a dark hardwood, perhaps oak.")
#item_dict["window"] = item("window", "You slowly move toward the window, and in the distance through the fog you can see the faint outline of what you think is something human")

#Main Room items

#item_dict["door"] = item("door", "The cold door is reinforced with wraught iron, leaving no way to break through.")
#item_dict["keyrack"] = item("keyrack", "There are no keys on the keyrack, but is worn down; implying the normal presence of a key")
#item_dict["painting"] = item("pinting", "It looks as if it is staring deep into your soul; penetrating your mind")

#Library items

#item_dict["bookshelf"] = item("bookshelf", "The bookshelf looms over you, filled with all the knowlegde. Along with my brand new Lamborghini")

#Dining Room items

#item_dict["table"] = item("table", "The table is cold. The remnants of food fill your nostrils, but see no signs of a recent dinner anywhere")
#item_dict["chair"] = item("chair", "The crude sun lounging chairs looks quite comfy, especially for eating. However, you feel like if you sat on the chairs, you would break it")
#item_dict["candles"] = item("candles", "The wax is warm to your skin, and the candle was lit recently.")
#item_dict["curtain"] = item("curtain", "The curtains blow in the wind, flapping calmly next to the window. After closer inspection, the window is not open..")

#"Conservatory?" items

#item_dict["plant"] = item("plant", "A potted plant. Quite cute")
#item_dict["rockinghorse"] = item("rockinghorse", "The horse is rocking. The horse is rocking...")

#Fountain items

#item_dict["fountain"] = item("fountain", "You're pretty sure this is the only functioning item in this house.")
#item_dict["doghouse"] = item("doghouse", "Was there a dog here? Who knows")
#item_dict["leaves"] = item("leaves", "A mess of leaves")

#Storage Room items

#item_dict["cage"] = item("cage", "The cage sits atop a shelf. Nearby there is a balance with a filled bucket dangling from it; making it lean to one side.")
#item_dict["rake"] = item("rake", "A nice rake, prime for raking", True)

#Non Findable items

#item_dict["lockpick"] = item("lockpick", "a lockpick. It picks locks", True, ["entrance_way"])
#item_dict["waterbucket"] = item("waterbucket", "its a bucket. it is filled with water and has some weight to it", False, ["store_cupboard"])

#item_dict["note1"] = item("note1", "add some lore", True)

world = {}
world["cellar"] = room("cellar", "A musty old cellar. How come you're down here? The cellar hatch is to the north. ", {"N": "kitchen"}, ["duck", "key", "dirt"], ["N"])
world["kitchen"] = room("kitchen", "An old kitchen, abandoned for years. There are some empty cupboards and a bucket. South is the cellar hatch, north lies a doorway to a room with coats hanging on a rack. East is the dining room. ", {"S": "cellar", "E": "dining_room", "N": "coat_racks"}, ["bucket", "cupboards", "oven", "knife"])
world["dining_room"] = room("dining room", "A dining room. Candles are burnt out, but fresh. The table lay bare, the eerie silence of the room disturbs you. West is the Kitchen. East is the conservatory to outside. ", {"W": "kitchen", "E": "BTECbalcony"}, ["table", "chair", "candles", "curtain"])
world["store_cupboard"] = room("store cupboard", "You see an old key in the corner of the room, locked in a cage. East is the fountain. ", {"E": "fountain"}, ["cage", "rake"])
world["fountain"] = room("fountain", "The crisp wind bites at your skin through your thin clothing. A fountain is in the middle of this small garden. West is the store cupboards and north is the conservatory. ", {"W": "store_cupboard", "N": "BTECbalcony"}, ["fountain", "doghouse", "leaves"])
world["BTECbalcony"] = room("conservatory", "The glass walls let little light through. ", {"W": "dining_room", "N": "library", "S": "fountain"}, ["plant", "rockinghorse"])
world["library"] = room("library", "A dusty library. Not much goes on here. South takes you to the conservatory, West to the entrance room, South is the conservatory. ", {"W": "entrance_way", "S": "BTECbalcony"}, ["bookshelf"])
world["coat_racks"] = room("coat room", "The room looks like a welcome room. In the corner there stands a coat rack with some coats on it. South is the kitchen, East is the entrance room. ", {"S": "kitchen", "E": "entrance_way"}, ["coats", "coatrack", "window"])
world["entrance_way"] = room("entrance way", "A moderately sized room with an exit to the outside world! West is the coat room, east is the library, and freedom is north! ", {"W": "coat_racks", "E": "library", "N": "exit"}, ["door", "keyrack", "painting"], ["N"])
world["exit"] = room("exit", "", {})

def show_help():
        print("")
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
        print("")
        print("When referring to any items with two words, leave no space in between e.g: keyrack")

def make_list(string):
        # makes a list of words from a string, seperated on spaces
        try:
                string = string.lower()
                word_list = string.split(" ")
                if "up" in word_list:
                        word_list.remove("up")
                return word_list
        except:
                print("String input was not a string")
                return []
        

def check_locked(direction):
        # being efficient with a function because I used this a fair bit
        if direction in player.current_room.locks:
                return True
        else:
                return False

def get_room_desc():
        # gets description of the player's current room
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
                # unlock the door and take the key away from the player
                player.current_room.locks.pop()
                player.inv.remove(item)
                print("The lock opens with an audible click, but your key crumbles to dust")
        elif item == "bucket":
                # fill the bucket with water
                player.inv.remove(item)
                player.inv.append("waterbucket")
                print("You fill the bucket with water from the fountain")
        elif item == "waterbucket":
                # "open the cage door" by adding the key to the items in the room
                player.inv.remove(item)
                world["store_cupboard"].items.append("key")
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
                                        print("You move to the other room.")
                        if word_list[i+1] in ref_dict["e"]:
                                if "E" in player.current_room.links:
                                        if check_locked("E"):
                                                print("The doorway is locked")
                                                break
                                        player.current_room = world[player.current_room.links["E"]]
                                        print("You move to the next room.")
                        if word_list[i+1] in ref_dict["s"]:
                                if "S" in player.current_room.links:
                                        if check_locked("S"):
                                                print("The doorway is locked")
                                                break
                                        player.current_room = world[player.current_room.links["S"]]
                                        print("You move to the next room.")
                        if word_list[i+1] in ref_dict["w"]:
                                if "W" in player.current_room.links:
                                        if check_locked("W"):
                                                print("The doorway is locked")
                                                break
                                        player.current_room = world[player.current_room.links["W"]]
                                        print("You move to the next room.")
                        break
                
                # take check
                elif word_list[i] in ref_dict["take"]:
                        #print("trying to pick up item")
                        if len(word_list) < i+2:
                                print("please specifiy something to take")
                                break
                        if len(player.current_room.items) > 0:
                                if word_list[i+1] in player.current_room.items and item_dict[word_list[i+1]].takable == True:
                                        print("picking up item " + word_list[i+1])
                                        player.inv.append(word_list[i+1])
                                        player.current_room.items.remove(word_list[i+1])
                                else:
                                        print("item not found, or you can't pick that up")
                        break

                # drop check
                elif word_list[i] in ref_dict["drop"]:
                        #print("trying to drop item")
                        if len(word_list) < i+2:
                                print("pleas specify something to drop")
                                break
                        if len(player.inv) > 0:
                                if word_list[i+1] in player.inv:
                                        player.inv.remove(word_list[i+1])
                                        player.current_room.items.append(word_list[i+1])
                                        print("Item " + word_list[i+1] + " dropped")
                                else:
                                        print("You can not drop this item as it is not in your inventory")
                        break
                
                # use check
                elif word_list[i] in ref_dict["use"]:
                        #print("using an item")
                        if len(word_list) < i+2:
                                print("Please specify an item to use")
                                break
                        if word_list[i+1] in player.inv and item_dict[word_list[i+1]].takable == True and player.current_room.name in item_dict[word_list[i+1]].usable_rooms: #or word_list[i+1] in player.current_room.items:
                                print("Using item " + word_list[i+1])
                                use(word_list[i+1])
                        else:
                                print("item not in inventory, or this is not the place to use that")

                        break
						
		# test checks converted to player-usable commands
                elif word_list[i] == "curr":
                        print(player.current_room.name)
                        break
                elif word_list[i] == "inv":
                        print(player.inv)
                        break

                # custom command checks
                elif word_list[i] == "sit":
                        if player.current_room.name == "dining room":
                                if word_list[i+1] == "chair" or word_list[i+1] == "chairs":
                                        print("You sit on the chair and it snaps. Told ya.")
                                        break
                                else:
                                        print("thats not a chair you are trying to sit on....")
                                        break
                elif word_list[i] == "rake":
                        if player.current_room.name == "fountain":
                                if (word_list[i+1] == "leaves" or word_list[i+1] == "leaf") and "rake" in playuer.inv:
                                        print("You rake the leaves and the ground is much tidier now. Good on you.")
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
print(item_dict["waterbucket"].usable_rooms)
while(gameRunning):
        playerInput = input("What do you do?")
        parse(make_list(playerInput))
        if (player.current_room.name == "exit"):
                gameRunning = False
                break
print("You feel the crisp winter air rush into your lungs")
print("What a nice feeling of calm")
print("The fog surrounding the building has dissipated all of a sudden")
print("and you can see clearly across the causeway.")
print("You march forward, still unsure why you were in there in the first place")
