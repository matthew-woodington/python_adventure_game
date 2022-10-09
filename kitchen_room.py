import time


class KitchenRoom():
    def __init__(self):
        self.has_key = False

    def set_key_found(self):
        self.has_key = True

    def start_kitchen(self):
        print(
            'You enter a dimly lit hallway just outside of your kitchen, walking foward...')
        time.sleep(3)
        print('You enter the kitchen. Your eyes focus on the current time on the stove.')
        time.sleep(3)
        print('Your heart sinks as you realize it is 10:45am on a Thursday!')
        time.sleep(3)
        print('Do you not have somewhere to be?')
        time.sleep(3)
        print('In a frantic panic you examine the kitchen.')
        time.sleep(3)

    def start_kitchen_again(self):
        time.sleep(1)
        print(
            'Your eyes come to focus and you realize you are somehow back in your kitchen.')
        time.sleep(3)
        print('You glance back at the stove and see that it is still 10:45am. How is this possible!')
        self.pick_ignore()

    def pick_ignore(self):
        print('You notice your phone on the kitchen table. Should you pick it up? Enter pick up or ignore:')
        choice_pick_ignore = input().lower()
        if choice_pick_ignore == 'pick up':
            print('You walk over to the kitchen table and pick up your phone.')
            self.pick_up()
        elif choice_pick_ignore == 'ignore':
            print(
                'You understand that the day is already well under way. Might as well try to enjoy it.')
            self.ignore()
        else:
            print('ENTER A VALID CHOICE! Pick up or ignore?')

    def pick_up(self):
        print('Your notice your phone has no new notifications. Not even an email. Peculiar...')
        time.sleep(3)
        print('You might as well enjoy your morning. You feel your stomach growl. How about breakfast?')
        time.sleep(3)
        print('Would you like to have breakfast? Type Yes or No.')
        pick_up_choices = input().lower()
        time.sleep(2)
        if pick_up_choices == 'yes':
            print(
                "A sandwich sounds great. Who says that breakfast has to be breakfast food anyway?")
            self.breakfast()
        elif pick_up_choices == 'no':
            print('You suppose it is getting close to lunch time. You will wait for now.')
            # insert new scenario to transition to here:
            self.breakfast_no()
        else:
            print('ENTER A VALID CHOICE! Choose Yes or No.')

    def ignore(self):
        time.sleep(2)
        print('With your hands on your hips, unsure how to spend your day, you hear the rustling of small feet shuffling around in the kitchen closet.')
        time.sleep(3)
        print('Would you like to investigate? Choose yes or no:')
        ignore_choices = input().lower()
        time.sleep(2)
        if ignore_choices == 'yes':
            print('Cautiously, you slowly approach the closet and crack the door open. Stumbling out is a 3 foot tall pink elephant.')
            time.sleep(3)
            self.investigate_yes()
        elif ignore_choices == 'no':
            print('You feel confused, thinking you must be seeing this, you saunter over to the kitchen table to pick up your phone.')
            time.sleep(3)
            self.pick_up()
        else:
            ('ENTER A VALID CHOICE! Choose yes or no:')

    def investigate_yes(self):
        print('Startled, the elephant yelps and scurries past you, managing to open and exit throught the back door.')
        time.sleep(3)
        print('Overcome with curiousity, you follow. Unable to see where exactly your new pick acquaintance went, you need to make a decision.')
        time.sleep(3)
        print(
            'Would you like to go left into the garden or right along the patio and pool?')
        time.sleep(2)
        print('Enter left or right:')
        follow_choices = input().lower()
        time.sleep(2)
        if follow_choices == 'left':
            print('You take a left turn and walk along the bushes in your garden.')
            time.sleep(3)
            self.choice_left()
        # CHOICE RIGHT

    def choice_left(self):
        print('About 15 paces ahead you notice what looks like a pink tail poking out from one of the bushes.')
        time.sleep(3)
        print('The elephant sees you approach. "Hello there! I didn\'t mean to disturb you. I got frightened and my natural instinct is to run off", it says.')
        time.sleep(4)
        print('"You seem friendly enough. My name is Emerson."')
        time.sleep(3)
        print('"Given the look on your face", he continues, "I am betting you are questioning your sanity by being addressed by a creature such as myself."')
        time.sleep(3)
        print('"I would like to help you. But first, let\'s have a little fun!", Emerson exclaims.')
        time.sleep(3)
        print('"True or false, you never catch a cold going up in an elevator?"')
        time.sleep(3)
        print('Enter true or false;')
        true_or_false = input().lower()
        time.sleep(1)
        if true_or_false == 'true':
            print('"Correct!", Emerson exclaims. "You come down with a cold, never up."')
            time.sleep(3)
            print('"Wasn\'t that fun?", your new pink friend giggles. "Now you are probably wondering what is going on."')
            time.sleep(2)
            print('"Trust me and take this with you. This will help you out very soon." Emerson vanishes into a cloud of smoke.')
            time.sleep(3)
            print(
                'At your feet appears a small metal fragment resembling a portion of a key.')
            time.sleep(3)
            print('Pick it up when you are ready...')
            self.ready_key()
        elif true_or_false == 'false':
            print('"So sorry! That is incorrect. Goodbye, friend!"')
            time.sleep(3)
            print('Emerson waves his arms towards you. Almost instantaneously you become severely fatigued and black out.')
            self.start_kitchen_again()

    def ready_key(self):
        time.sleep(2)
        print('Type continue when you are ready:')
        ready_go = input().lower()
        if ready_go == 'continue':
            print('You pick up the metal key fragment. You swiftly become engulfed in bright cosmic energy. You vanish into the abyss...')
            return
        else:
            print('ENTER A VALID CHOICE! Type continue when you are ready.')

    def breakfast(self):
        print('You gather together the ingredients for a glorious sandwich.')
        time.sleep(3)
        print('Your stomach reassures you that bacon would make a fantastic addition.')
        time.sleep(3)
        print('You turn on the stove and slap a few slices of greasy goodness onto a pan.')
        time.sleep(3)
        print('Only a few minutes away from glory!')
        time.sleep(3)
        print('Unexpectedly pained by a headache, you decide to lay on the couch to close your eyes.')
        time.sleep(3)
        print('You fall asleep...')
        time.sleep(10)
        print('Suddenly you are awakened by the sound of blaring smoke alarms. THE BACON!')
        time.sleep(3)
        print('You run to your kitchen closet and within is a tiny pink elephant leaning against the fire extinguisher.')
        time.sleep(3)
        print("It just waved at you. IT'S ALIVE?!")
        time.sleep(3)
        print('No time to think about this! You grab the fire extinguisher and swiftly diminish the flames. Crisis averted.')
        time.sleep(5)
        print('As your heart rate begins to slow down you remember the strange thing you saw in the closet next to the fire extinguisher.')
        time.sleep(3)
        print('Would you like to investigate or go outside for fresh air? Enter investigate/outside:')
        breakfast_choices = input().lower()
        time.sleep(2)
        if breakfast_choices == 'investigate':
            print(
                'You walk over to the closet and open the door. There is nothing in here...')
            time.sleep(3)
            # go back to a previous function
        elif breakfast_choices == 'outside':
            print("You walk out into the back yard wiping sweat from your brow. You hear what sounds like a child's laughter coming from the bushes.")
            time.sleep(3)
            print("Emerging is a 3 foot tall pink elephant. Smiling, he says ''You made it! Nice job. Here, take this with you.''")
            time.sleep(3)
            print('He hands you what appears to be a piece of a key. Your headache suddenly comes back, hurting twice as bad as before.')
            time.sleep(2)
            print('You become overwhelmingly light-headed. You black out...')
            return
        else:
            print('ENTER A VALID CHOICE! Choose investigate or outside.')

    def breakfast_no(self):
        time.sleep(2)
        breakfast_no_choices == input().lower()


# def play_kitchen_room():
#     kitchen_room = KitchenRoom()

#     kitchen_room.start_kitchen()
#     kitchen_room.pick_ignore()
#     player.add_key()


# play_kitchen_room() # just here for testing purposes. delete before final push!
