
key_fragments = 0

def start_room()

    if key_fragments == 0:
        print("First time in start room/start of game")
    elif key_fragments == 1:
        print("start room again. seems familiar. have part of key")
    elif key_fragments == 2:
        print("start room again. why does this keep happening?. have 2 pieces of broken key.")
    elif key_fragments == 3:
        print("start room for last time. worry might go on forever. key fragments snap together. final door glows and unlock.")

    choice = input("What door do you open? (left/right/ahead/behind:  ").lower()

    if choice == left :
        {door_one}
    elif choice == right :
        {door_two}
    elif choice == ahead :
        {door_three}
    elif choice == behind :
        if key_fragments < 3 :
            print("this door is locked")
        else:
            print("door opens")
            print("all in your head...")
            print("thanks for playing")
            break