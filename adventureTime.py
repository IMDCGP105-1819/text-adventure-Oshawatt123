ref_dict = {"n": ["north", "forward", "upward"], "s": ["south", "back", "backward"],
            "take": ["take", "grab", "pick"], "items": ["key", "lokcpick", "bucket", "duck"],
            "look": ["look", "search"]}

class gameManager():
        
        def __init__(self):
                print("lol made")

def make_list(string):
        
        string = string.lower()
        return string.split(" ")

def parse(word_list):
        i = 0
        print(word_list)
        while i < len(word_list):
                if word_list[i] in ref_dict["look"]:
                        print("looking around")
                        break
                elif word_list[i] == "go":
                        if word_list[i+1] in ref_dict["n"]:
                                print("going north")
                                break
                        #east
                        #south
                        #zip
                elif word_list[i] in ref_dict["take"]:
                        print("trying to pick up item")
                        if word_list[i+1] in ref_dict["items"]:
                                print("trying to pick up item " + word)
                                break
                else:
                        break
        i += 1

gameRunning = True
while(gameRunning):
        playerInput = input("What do you do?")
        parse(make_list(playerInput))
        
