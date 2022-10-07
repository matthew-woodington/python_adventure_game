import time
# Might not need the "here_before" variable in many cases.
class KitchenRoom():
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    def start_kitchen():
        print("You enter a dimly lit hallway just outside of your kitchen.")
        print("")

    def pick_ignore():
        print("""
            You enter the kitchen. Your eyes focus on the current time on the stove. 
            Your heart sinks as you realize it is 10:45am on a Thursday! Don't you have
            somewhere to be? In a frantic panic you examine the kitchen. You notice 
            your phone on the kitchen table. Should you pick it up?
             
            Type your choice: Pick Up, or Ignore.
             
            """)
        ans1 = input(">> ").lower()
        time.sleep(2)
        if(ans1()=="pick up"):
            print("\nYou walk over to the kitchen table and pick up your phone.")
            pickup()
        elif(ans1()=="ignore"):
            print("You understand that the day is already well under way. Might as well try to enjoy it.")
            ignore()
        else:
            print("ENTER A VALID CHOICE! Pick up or ignore?")
            ans1 = input(">> ").lower()
    def pickup():
        print("""
                Your notice your phone has no new notifications. Not even an email. Peculiar...""")
        time.sleep(1)
        print("""
            You might as well enjoy your morning. You feel your stomach growl. How about breakfast?
            
            Would you like to have breakfast? Type Yes or No.
            
            """)
        ans2 = input(">> ").lower()
        time.sleep(2)
        if(ans2() == "Yes"):
            print("A sandwich sounds great. Who says that breakfast has to be breakfast food anyway?")
            breakfast()
        elif(ans2()== "No"):
            print("I guess it is getting close to lunch time. I will wait for now.")
            # insert new scenario to transition to here:
            breakfast_no()
        else:
            print("ENTER A VALID CHOICE! Choose Yes or No.")
            ans2 = input(">> ").lower()
    def breakfast():
        print("""
            You gather together the ingredients for a glorious sandwhich. Your stomach reassures you
            that bacon would make a fantastic addition. You turn on the stove and slap a few slices
            of greasy goodness onto a pan. Only a few minutes away from glory!
            Unexpectedly pained by a headache, you decide to lay on the couch to close your eyes.
            You fall asleep.""")
        time.sleep(15)
        print("""
            Suddenly you are awakened by the sound of blaring smoke alarms. THE BACON!""")
        time.sleep(3)
        print("""
            You run to your kitchen closet and within is a tiny pink teddy bear leaning againt
            the fire extinguisher. It just waved at you. IT'S ALIVE?! 
            No time to think about this! You grab the fire extinguisher and swiftly diminish the
            flames. Crisis averted.""")
                #more conditions for breakfast and elephant.

    def breakfast_no():
        time.sleep(2)