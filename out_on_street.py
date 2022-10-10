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

    def visited_places(self):
        self.visited_places_items.append(self.visited)


    def on_street(self):
            system('clear')
            print("You are out of your house walking on the street it is sunny", end=" ") 
            print("and warm. The street looks quiet you fell like you are the only one walking around.... \n ", flush = True)
            time.sleep(2)
            print("You are feeling something is on the air, a nice breath brushed your face. Oh what a nice feeling", end =" ", flush=True)
            time.sleep(2)
            print("You start to look around thinking there are lot of places that you may go to....", flush = True)
            time.sleep(2)
            print("Just across the street in front of you there is a nice cafe. You may walk to the park if you just head south to your left", end=" ", flush = True)
            print("north of here to the right there is a nice ice cream place. What a day to chose what to do....", flush = True)
            time.sleep(2)
            print("Which direction will you go: \n<left  >right  ^forward \n", flush = True)
            self.direction = input('').lower()
            self.answer = 'incorrect'
            self.available_directions = ['left','right','forward']
            self.cycle_route= 0
            self.action_directions()
            self.visited_places_items=[]


    def route_checker(self):
        if (self.available_directions==[]) and (self.has_key == False):
            self.available_directions = ['left','right','forward']
            self.cycle_route = self.cycle_route+1
            self.available_directions.remove(self.direction)
            return self.available_directions
        if self.cycle_route > 4:
            print('It looks like nothing is catching your interest. Do you want to go back to where you started?')
            print('Do you want to go back or need a hint?')
            self.checker =['back', 'hint']
            self.input_checker()
            response = self.response 
            if response == 'hint':
                print('Check any action other than ignore.... ')
                self.cycle_route=0
                return self.available_directions
            elif response == 'back':
                self.action_saved()
                return 


    def action_directions(self):
        while self.answer == 'incorrect':
            direction = self.direction
            if direction == 'left':
                self.route_checker()
                print("What a lovely day to spend in the park.")
                # print(self.available_directions)
                # time.sleep(1)
                print("You started to walk, you are hearing some stange sounds. I seems like someone is calling you, how come you " , end= "", flush = True)
                time.sleep(1.5)
                print("can't see anyone around, but still someone is calling. Looking around then you raised your head. Now!",end =" ", flush = True)
                time.sleep(2)
                print("You see there is a stranded cat on a tree you just passed. ",end="", flush = True)
                time.sleep(.4)
                print("You noticed that it was not able to come down. She started to mewo and looked scared. How easy for a cat to go up a tree while scary to get down .... Oh no that is hard!", flush = True)
                time.sleep(1.5)
                print('She is looking toward you blinking her eyes. Begging you to help....', end=" ", flush = True)
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
                print("Hey going for ice cream topping the nice weather with great sweet taste (: .", flush = True)
                time.sleep(2)
                print('You started walking,you can not believe your eyes it looks like everyone is gathering at that icecream place you are heading to.', end=" ", flush = True)
                time.sleep(3)
                print('It looks like some type of festival or celebration......\nYou wonder if there is special event or celebration??', end=" ", flush = True)
                time.sleep(3)
                print('Maybe after all it will be your lucky day to meet someone you know and have a good time? \n Do you want to continure towards the ice cream place or go back?', flush = True)
                self.answer = 'correct'
                self.checker =['continue', 'back']
                self.input_checker()
                response = self.response
                if response == 'continue':
                    self.right_jenny()
                elif response == 'back':
                    self.action_from_direction()

            elif direction == "forward":
                self.route_checker()
                print('You are crossing the street toward the cafe, as you are walking ', end= "" , flush = True)
                time.sleep(1.5)
                print('you see on the news stand at the corner, some newspapers. ', end="", flush = True )
                time.sleep(1.5)
                print("You can see some headlines on todays newspaper, it is not clear it looks blury you think it have something to do with these empty streets...hummmm? ", flush = True) 
                time.sleep(1.5)
                print("There is a picture with the headline, something is familiar to you about it.......", flush = True)
                time.sleep(1.5)
                print("It cought your attention!! May be it have an answer to what is happening around you or may be to you???", flush = True)
                time.sleep(1.5)
                print("Do you want to get closer and read it? or continue to the cafe pick your destiny.........", flush = True)
                self.answer = 'correct'
                self.checker =['read', 'cafe']
                self.input_checker()
                response = self.response
                if response == 'read':
                    print("You came closer and the face you see on the picture looks like..... ", end="", flush=True)
                    time.sleep(3)
                    print("somewhat familiar... Yes!YEs!!!YEEESSS!!!", flush=True)
                    time.sleep(3)
                    print("That is JENNY!!! What just happened why is she on the front page.", end=" ", flush=True)
                    time.sleep(2)
                    print("You are looking on the paper and suddenly ....you are....")
                    time.sleep(1)
                    self.right_park()
                elif response == 'cafe':
                    print("You went on your way to the cafe, ordered your coffee sat there for some time. It is", end=" ",flush=True)
                    time.sleep(2)
                    print("type boring with no one to chat with. You walked bak to the street and now.", end=" ", flush=True)
                    self.action_from_direction()  
            else:
                print('Please pick a valid entry')
                self.direction = input('').lower()
                continue


    def action_help(self):
        time.sleep(1)
        print("You started to look around to find a way to reach her.You started to think about what", end=" ")
        time.sleep(.7)
        print("can you do to help her. You thought may be you will climb the tree to save her or get a ladder!\n", end=" ")
        time.sleep(.7)
        print("What will be your first choice?  \nget a ladder  \nclimb the tree?\n")
        time.sleep(1)
        self.checker =['climb', 'ladder']
        self.input_checker()
        response = self.response 
        if response == 'climb':
            self.action_climb()
        elif response == 'ladder':
            self.action_saved()

    def action_climb(self):
        time.sleep(1)
        print('You started to extend your arms to give her a soft pad to jump into.', end=" ")
        time.sleep(1)
        print("She was still scared and didn't move, while she is still calling you to help.", end = " ")
        time.sleep(1)
        print("You started to climb the tree, now the sweet memories of your childhood started to fill you,", end= " ")
        time.sleep(1)
        print("you extended your arms agin to reach for the cat. Were you able to get her ?")
        self.checker =['yes', 'no']
        self.input_checker()
        response = self.response 
        if response == 'yes':
            self.action_saved()
        elif response == 'no':
            self.action_not_reached()

    def action_not_reached(self):
        time.sleep(2)
        print('Oh no what a hard job you had. Do you want to get a ladder to help this poor cat?', end =" ", flush = True)
        time.sleep(1)
        print("She sounds stressed, may be a ladder will help you reach where she is at.", flush = True)
        time.sleep(1)
        print("Do you want to find a ladder or continue on your way?", flush = True)
        self.checker =['ladder', 'continue']
        self.input_checker()
        response = self.response
        if response == 'ladder':
            self.option_ladder()
        elif response == 'continue':
            self.ction_from_direction()

    def action_saved(self):
        time.sleep(3)
        print('Oh what a great job and nice effort. The cat stared to wisper something into your ear,',end=" ", flush = True)
        time.sleep(1)
        print("while noding her head, she is now safe. What you want to do next let her go or find if it have an owner tag?", flush = True)
        self.checker =['tag', 'go']
        self.input_checker()
        response = self.response
        if response == 'tag':
            print('You started to look at the tag on her collar it have some type of glow that pulled you into....')
            time.sleep(2)
            print("a deep place your start to feel like ...like.....")
            self.set_key_found()
        elif response == 'go':
            self.action_from_direction()

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
        print("You start to walk toward the icecream place, people are having a blast", end =" ", flush = True)
        time.sleep(2)
        print("kids are playing around adults are chatting. You think you can see Jenny your friend in high school. You didn't know she", end =" ", flush = True)
        time.sleep(3)
        print("is back in town since she move to another state 3 years ago. What a nice day, you had lots",  end=" ", flush = True) 
        time.sleep(2)
        print("of memories with her, wouldn't it be nice to go an say hello? You started to walk toward her dirction waving your hand", end=" ", flush = True)
        time.sleep(2)
        print("while you were moving on your way trying to catch her attention she turned around....\n\n   Do you think she saw you?", flush = True)
        self.checker =['yes', 'no']
        self.input_checker()
        response = self.response 
        if response == 'yes':
            self.right_did_see()
        elif response == 'no':
            self.right_not_see()

    def right_did_see(self):
        print("She waved back to you, you started to chat you told her how you started this day and all the options that you thought about", end =" ", flush = True)
        time.sleep(3)
        print(",she said she like to have an ice cream cone. Then she said the place is realy crowded may be we go for a walk then come to have the ice cream later.", flush = True)
        time.sleep(3)
        print('What you want to do go to the park or have ice cream?', flush = True)
        self.checker =['park', 'ice cream']
        self.input_checker()
        response = self.response 
        if response == 'park':
            self.right_park()
        elif response == 'ice cream':
            self.right_ice_cream()

    def right_not_see(self):
        print("Oh no Jenny did't see you and got into a cap that has just pulled in.", end =" ", flush = True)
        time.sleep(3)
        print("After all you may still go into the ice cream place and enjoy the icy creamy delight", flush = True )
        time.sleep(2)
        print("Do you want to get in and order or just go back")
        self.checker =['order', 'go back']
        self.input_checker()
        response = self.response 
        if response == 'order':
            self.right_ice_cream()
        elif response == 'go back':
            self.action_from_direction()

    
    def right_ice_cream(self):
        print('You got in, there are a lot of varieties to choose from. But you know what you likes best', end=" ", flush = True)
        time.sleep(2)
        print("You took a big scoop out of your cup.... You see a flash of light ")
        self.action_from_direction()

    def right_park(self):
        print("You and Jenny are walking towards the park. You were talking about all the memories that you had and the class", end = " ", flush = True)
        time.sleep(3)
        print("joks that were... It seems that you started to teleport to that time and now you were walking in your high school hall!!! ", end= " ", flush = True)
        time.sleep(3)
        print("You are walking toward the main entrance where the sun light is coming through,then you looked to you left and " , end =" ", flush = True)
        time.sleep(2)
        print("there, the stairs to the second floor. She was telling to walk with her toward the exit she didn't like it in here. You wanted to go upstairs and visit your old class", end= " ")
        time.sleep(3)
        print("\n  Will you exit or go up the stairs?", flush = True)
        self.checker =['exit', 'stairs']
        self.input_checker()
        response = self.response 
        if response == 'exit':
            print("You hear someone talking to you in a deamy vice .... is it some hidden message", flush = True)
            time.sleep(4)
            print("BAM!!!!! ")
            time.sleep(2)
            print("There comes a light and you hear...")
            self.action_saved()
        elif response == 'stairs':
            self.action_not_reached()

    




# def play_OutOnStreet():
#     outOnStreet = OutOnStreet()
#     outOnStreet.on_street()

# play_OutOnStreet()        





