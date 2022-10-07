class KitchenRoom():

    def scenario1():
        import time
        print("""
            You enter the kitchen. Your eyes focus on the current time on the stove. 
            Your heart sinks as you realize it is 10:45am on a Thursday! Don't you have
             somewhere to be? In a frantic panic you examine the kitchen. You notice 
             your phone on the kitchen table. Should you pick it up?
             
             Type your choice: Pick Up, or Ignore.
             
             """)

        c1 = input ()
        time.sleep(2)
        ans = 'incorrect'
        while(ans=='incorrect'):
            if(c1.lower()=="pick up"):
                print("\nYou walk over to the kitchen table and pick up your phone.")
                ans = 'correct'
                time.sleep(1)
            elif(c1.lower()=="ignore"):
                print("You understand that the day is already well under way. Might as well try to enjoy it.")
            else:
                print("ENTER A VALID CHOICE! Pick up or ignore?")
                c1 = input ()