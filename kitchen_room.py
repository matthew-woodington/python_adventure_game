import time

class KitchenRoom():
    def __init__(self):
        self.has_key = False
    
    def set_key_found(self):
        self.has_key = True

    def start_kitchen(self):
        print('You enter a dimly lit hallway just outside of your kitchen, walking foward...')
        time.sleep(3)
        print('You enter the kitchen. Your eyes focus on the current time on the stove.')
        time.sleep(3)
        print('Your heart sinks as you realize it is 10:45am on a Thursday!') 
        time.sleep(3)
        print('Do you not have somewhere to be?') 
        time.sleep(3)
        print('In a frantic panic you examine the kitchen.')
        time.sleep(3)
        
    def pick_ignore(self):
        print('You notice your phone on the kitchen table. Should you pick it up? Enter pick up or ignore:')
        choice_pick_ignore = input().lower()
        if choice_pick_ignore =='pick up':
            print('You walk over to the kitchen table and pick up your phone.')
            self.pick_up()
        elif choice_pick_ignore == 'ignore':
            print('You understand that the day is already well under way. Might as well try to enjoy it.')
            self.ignore()
            # still need ignore choice event
        else:
            print("ENTER A VALID CHOICE! Pick up or ignore?")
            
    def pick_up(self):
        print("""
                Your notice your phone has no new notifications. Not even an email. Peculiar...""")
        time.sleep(3)
        print("""
            You might as well enjoy your morning. You feel your stomach growl. How about breakfast?
            
            Would you like to have breakfast? Type Yes or No.
            
            """)
        pick_up_choices = input().lower()
        time.sleep(2)
        if pick_up_choices == 'yes':
            print("A sandwich sounds great. Who says that breakfast has to be breakfast food anyway?")
            self.breakfast()
        elif pick_up_choices == 'no':
            print('You suppose it is getting close to lunch time. You will wait for now.')
            # insert new scenario to transition to here:
            self.breakfast_no()
        else:
            print('ENTER A VALID CHOICE! Choose Yes or No.')
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
        print("""
            You run to your kitchen closet and within is a tiny pink teddy bear leaning againt
            the fire extinguisher. It just waved at you. IT'S ALIVE?! 
            No time to think about this! You grab the fire extinguisher and swiftly diminish the
            flames. Crisis averted.""")
                #more conditions for breakfast and elephant.

    def breakfast_no():
        time.sleep(2)

def play_kitchen_room():
    kitchen_room = KitchenRoom()

    kitchen_room.start_kitchen()
    kitchen_room.pick_ignore()


play_kitchen_room()