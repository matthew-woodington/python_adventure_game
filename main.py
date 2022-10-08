import time
from hospital import HospitalRoom
from out_one_street import OutOnStreet

class Player():
    def __init__(self):
        self.key_fragments = 0

    def add_key(self):
        self.key_fragments += 1


player = Player()

def play_hospital_room():
    hospital_room = HospitalRoom()
    hospital_room.room_start()
    hospital_room.main_room_view()
    player.add_key()
    print(player.key_fragments)

def play_OutOnStreet():
    outOnStreet = OutOnStreet()
    outOnStreet.on_street()
    player.add_key()


def start_room():

    if player.key_fragments == 0:
        print("You find yourself lying flat on your back. You look straight up, but can only see what seems to be endless darkness. You go begin to sit up and try to get your bearings.")
        time.sleep(3)
        print("All you are able make out in the darkness is the dim glow of light framing an antique looking wood door. As you look around you notice three more identical doors surrounding you, though the one behind you has no light.")
        time.sleep(3)
        print("As your eyes begin to adjust to the darkness, you can see that you are in a small empty room with pitch black walls that seem to go on forever.")
        time.sleep(3)
        print("It appears that your only options for escape are the doors. You decide to approach one.")
        time.sleep(3)
    elif player.key_fragments == 1:
        print("Your eyes snap open, expecting to see the world around you, but are instead greeted with infinite darkness. Somehow you've returned to the dark room of doors.")
        time.sleep(3)
        print("You feel cool metal reasting in your palm. You look down to see a small piece of a broken key. It can't do much in it's current state.")
        time.sleep(3)
        print("You must pick another door to try.")
        time.sleep(3)
    elif player.key_fragments == 2:
        print("Everything around you fades to black, and you have trouble seeing. After a moment your surroundings begin to take shape.")
        time.sleep(3)
        print("Once again you find yourself in the pitch black room of doors. 'What is this place? How do I keep ending up here?', you ask yourself as you clutch the now two key fragments tightly.")
        time.sleep(3)
        print("There is no use staying here. You must continue to try the doors.")
        time.sleep(3)
    elif player.key_fragments == 3:
        print("You feel a familiar sensation as all around you turns to black. You recognise immediately that you have returned to the room of doors.")
        time.sleep(3)
        print("You fear that this cycle may go on forever. An infinite loop of confusion and horror. But, you cannot give up. You must venture on.")
        time.sleep(3)
        print("You notice that the room is just a bit brighter than before. You realize that the door behind you now has a warm glow coming from behind it and the key that was once in pieces has somehow become whole.")
        time.sleep(3)
        print("Your only choice is to keep moving forward.")
        time.sleep(3)

    choice = input(
        "Which door do you try to open? left/right/ahead/behind:  ").lower()

    if choice == 'left':
        print("You open the door and step through.")
        time.sleep(3)
        play_hospital_room()
    elif choice == 'right' :
        print("You open the door and step through.")
        time.sleep(3)
        play_OutOnStreet()
    elif choice == 'ahead':
        print("You open the door and step through.")
        time.sleep(3)
        {door_three}
    elif choice == 'behind':
        if player.key_fragments < 3:
            print(
                "You try to turn the handle but it will not budge. This door is locked.")
            time.sleep(3)
        else:
            print("You insert the reformed key into the door and turn the handle. The door swings open and emits a warm, blinding light. You step through.")
            time.sleep(3)
            print("The darkness you've grown accustomed to vanishes in an instant. You feel overwhelmed as your senses are bombarded with the sudden change. Your eyes are closed and you are hesitant to open them.")
            time.sleep(3)
            print("After a moment, you open eyes and discover you are lying in a hospital bed, surrounded by your friends and family.")
            time.sleep(3)
            print("You ask what happened and they tell you that you were in a terrible accident. They haven't left your side since and could tell that you were fighting to come back to them the whole time.")
            time.sleep(3)
            print("Congratulations, you've made it home after piecing your mind back together.")
            time.sleep(3)
            print("Thanks for playing!")
            return
    else:
        print("Please enter a valid response.")
        time.sleep(3)

start_room()