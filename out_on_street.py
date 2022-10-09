# You are walking down the street it looks just like the one out of your door
# feeling
import time
import typing
from os import system

class OutOnStreet():
    def __init__(self):
        self.has_key =False

    def set_key_found(self):
        self.has_key = True
        return

    def on_street(self):
            system('clear')
            print("""You are out of your house walking on the street it is sunny 
and warm. The street looks quiet you fell like you are the only one walking around.... \n """)
            time.sleep(3)
            print("You are feeling something is on the air, a nice breath brushed your face. Oh what a nice feeling", end =" ")
            time.sleep(3)
            print("You start to look around \nthinking there are a lot of places that you may go to....")
            time.sleep(2)
            print("Just across the street in front of you there is a nice cafe. You may walk to the park if \n you just head south to your left", end=" ")
            print("north of here to the right there is a nice icecream place. What a day to chose what to do....")
            time.sleep(2)
            print("Which direction will you go: \n<left  >right  ^forward \n")
            self.direction = input('').lower()
            self.answer = 'incorrect'
            self.available_directions = ['left','right','forward']
            self.cycle_route= 0
            self.action_directions()


    def route_checker(self):
        if (self.available_directions==[]) and (self.has_key == False):
            self.available_directions = ['left','right','forward']
            self.cycle_route = self.cycle_route+1
        self.available_directions.remove(self.direction)
        if self.cycle_route > 2:
            print('It looks like nothing is catching your interest. Do you want to go back to where you started?')
            print('Do you want to go back or need a hint?')
        self.checker =['back', 'hint']
        self.input_checker()
        response = self.response 
        if response == 'hint':
            print('Check any action other than ignore.... ')
            self.available_directions
        elif response == 'back':
            self.action_saved()
            return 


    def action_directions(self):
        while self.answer == 'incorrect':
            direction = self.direction
            if direction == 'left':
                self.route_checker()
                print(self.available_directions)
                time.sleep(1)
                print('There is a stranded cat on a tree. ',end="")
                time.sleep(1.5)
                print("You noticed that it was not able to come down. She started to mewo and looked scared.")
                time.sleep(1.5)
                print('She is looking toward you blinking her eyes.', end=" ")
                print('What you want to do? \n\n Help  /   Ignore')
                self.answer = 'correct'
                self.checker =['help', 'ignore']
                self.input_checker()
                response = self.response
                if response == 'help':
                    self.action_help()
                elif response == 'ignore':
                    self.action_from_direction()

            elif direction == "right":
                self.route_checker()
                print('You see some crowd on the far side of the street. they are gathering close to that icecream \nplace that you thought about visiting.', end=" ")
                time.sleep(3)
                print('It looks like some type of festival or celebration......\n you wonder if there is specila event or national celebration??  ')
                time.sleep(3)
                print('Maybe you meet someone you know and have a good time? \n Do you want to go and check  or ignore?')
                self.answer = 'correct'
                self.checker =['check', 'ignore']
                self.input_checker()
                response = self.response
                if response == 'check':
                    self.right_check()
                elif response == 'ignore':
                    self.action_from_direction()

            elif direction == "forward":
                self.route_checker()
                print('There is a news stand in front of you')
                time.sleep(2)
                print("""You can see some head lines on todays news paper. it is not clear\n
it looks blury you think it have something to do with these empty streets...hummmm? """) 
                time.sleep(2)
                print("There is a picture with the headline there is something familiar to you about it.......")
                time.sleep(2)
                print("There is something about it that cought your attention!!")
                time.sleep(2)
                print("Do you want to get closer and read it? May be it give you a clue about \nwhat is going on around you... \n  Do you ignore it?")
                self.answer = 'correct'
                self.checker =['read', 'ignore']
                self.input_checker()
                response = self.response
                if response == 'read':
                    self.forward_check()
                elif response == 'ignore':
                    self.action_from_direction()  
            else:
                print('Please pick a valid entry')
                self.direction = input('').lower()
                continue


    def action_help(self):
        time.sleep(1)
        print("""You started to look around to find a way yo reach her.You started to think about what 
can you do to help her. You thought may be you will climb the tree to save her or get a ladder!\n
What will be your first choice?  \nget a ladder  \nclimb the tree?\n""")
        time.sleep(3)
        self.checker =['climb', 'ladder']
        self.input_checker()
        response = self.response 
        if response == 'climb':
            self.action_climb()
        elif response == 'ladder':
            self.action_saved()

    def action_climb(self):
        time.sleep(1)
        print('Can you reach the cat \nYes  \n\nNo')
        self.checker =['yes', 'no']
        self.input_checker()
        response = self.response 
        if response == 'yes':
            self.action_saved()
        elif response == 'no':
            self.action_not_reached()

    def action_not_reached(self):
        time.sleep(2)
        print('Do you want to get a ladder or go on with your business. ')
        self.checker =['ladder', 'go']
        self.input_checker()
        response = self.response
        if response == 'ladder':
            self.option_ladder()
        elif response == 'go':
            self.action_from_left()

    def action_saved(self):
        time.sleep(3)
        print('Oh great you saved a cat that was awsome. Did you notice what color is this cat? \nWhite \nOther ')
        self.checker =['white', 'other']
        self.input_checker()
        response = self.response
        if response == 'white':
            self.set_key_found()
        elif response == 'other':
            self.action_from_left()

    def action_from_direction(self):
        if len(self.available_directions) <1:
            self.route_checker()
        time.sleep(1)
        print("You are back in front of your house on the street....  ")
        time.sleep(1)
        if len(self.available_directions)==2:
            print("Where do you want to go:\n",self.available_directions[0],"\n",self.available_directions[1])
            time.sleep(1)
            self.checker =[self.available_directions[0], self.available_directions[1]]
        else:
            self.checker =[self.available_directions[0], self.available_directions[0]]
        self.answer = 'incorrect'
        self.input_checker()
        self.direction = self.response
        self.action_directions()


    def input_checker(self):
        mistake_counter=0
        if self.checker[0]==self.checker[1]:
            print("\n Please enter ",self.checker[0],"  ")
            
        print("\n Please enter ",self.checker[0],"/",self.checker[1],"  ")
        self.response = input(" >> ")
        ask_to_correct = True
        if (self.response == self.checker[0]) or (self.response == self.checker[1]):
            ask_to_correct =  False
        while ask_to_correct == True:
            mistake_counter= mistake_counter+1
            if mistake_counter > 17:
                time.sleep(3)
                print("Lets get back to the main game")
                return
            if mistake_counter > 8:
                print("May be you need to check your inputs !")
            print("Please enter ",self.checker[0],"/",self.checker[1]," >> ")
            self.response = input(" >> ")
            if (self.response == self.checker[0]) or (self.response == self.checker[1]):
                ask_to_correct =  False
                return self.response


    def right_jenny(self):
        print("""You start to walk toward the icecream place, people are having a blast
kids are playing around adults are chatting. You think you can see Jenny your \nfriend since high school. You didn't know she""", end =" ")
        time.sleep(3)
        print("is back in town since she move to another state 3 years ago. What a nice day you had lots",  end=" ") 
        time.sleep(2)
        print("of memories with her, wouldn't it be nice to go an say hello? You started to \n walk toward her dirction waving your hand", end=" ")
        time.sleep(2)
        print("")
    def right_icecream(self):
        print('You and Jenny')

    def right_park(self):
        print('')

    




# def play_OutOnStreet():
#     outOnStreet = OutOnStreet()
#     outOnStreet.on_street()

# play_OutOnStreet()        





