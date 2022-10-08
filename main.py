import time


key_fragments = 0

def start_room()

    if key_fragments == 0:
        print("You find yourself lying flat on your back. You look straight up, but can only see what seems to be endless darkness. You go begin to sit up and try to get your bearings.")
        time.sleep(3)
        print("All you are able make out in the darkness is the dim glow of light framing an antique looking wood door. As you look around you notice three more identical doors surrounding you, though the one behind you has no light.")
        time.sleep(3)
        print("As your eyes begin to adjust to the darkness, you can see that you are in a small empty room with pitch black walls that seem to go on forever.")
        time.sleep(3)
        print("It appears that your only options for escape are the doors. You decide to approach one.")
        time.sleep(3)
    elif key_fragments == 1:
        print("Your eyes snap open, expecting to see the world around you, but are instead greeted with infinite darkness. Somehow you've returned to the dark room of doors.")
        time.sleep(3)
        print("You feel cool metal reasting in your palm. You look down to see a small piece of a broken key. It can't do much in it's current state.")
        time.sleep(3)
        print("You must pick another door to try.")
        time.sleep(3)
    elif key_fragments == 2:
        print("Everything around you fades to black, and you have trouble seeing. After a moment your surroundings begin to take shape.")
        time.sleep(3)
        print("Once again you find yourself in the pitch black room of doors. 'What is this place? How do I keep ending up here?', you ask yourself as you clutch the now two key fragments tightly.")
        time.sleep(3)
        print("There is no use staying here. You must continue to try the doors.")
        time.sleep(3)
    elif key_fragments == 3:
        print("You feel a familiar sensation as all around you turns to black. You recognise immediately that you have returned to the room of doors.")
        time.sleep(3)
        print("You fear that this cycle may go on forever. An infinite loop of confusion and horror. But, you cannot give up. You must venture on.")
        time.sleep(3)
        print("You notice that the room is just a bit brighter than before. You realize that the door behind you now has a warm glow coming from behind it and the key that was once in pieces has somehow become whole.")
        time.sleep(3)
        print("Your only choice is to keep moving forward.")
        time.sleep(3)

    choice = input("Which door do you try to open? left/right/ahead/behind:  ").lower()

    if choice == 'left' :
        print("You open the door and step through.")
        time.sleep(3)
        {door_one}
    elif choice == 'right' :
        print("You open the door and step through.")
        time.sleep(3)
        {door_two}
    elif choice == 'ahead' :
        print("You open the door and step through.")
        time.sleep(3)
        {door_three}
    elif choice == 'behind' :
        if key_fragments < 3 :
            print("this door is locked")
            time.sleep(3)
        else:
            print("door opens")
            time.sleep(3)
            print("all in your head...")
            time.sleep(3)
            print("thanks for playing")
            break
    else:
        print("Please enter a valid response.")
        time.sleep(3)