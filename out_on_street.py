# You are wlaking down the street it looks just like the one out of your door
# feeling 
import time

class OutOnStreet():

    def __init__(self):
            self.has_key = False
    
    def set_key_found(self):
            self.has_key = True

    def on_street(self):

        print("You are out of your house walking on the street it is sunny and warm. The street looks quite you are the only one walking around....  ")
        time.sleep(3)
        print("Where do you want to go: \n<left \n>right \n^forward")
        self.direction = input('').lower()
    
        self.answer = 'incorrect'
        self.action_directions()

    def action_directions(self):

        while self.answer == 'incorrect':
            direction = self.direction

            if direction == 'left':
                print('There is a stranded cat on the tree.')
                print('What you want to do? \nHelp \nIgnore')
                response = input('').lower()
                if response == 'help':
                    self.action_help()
                elif response == 'ignore':
                    self.action_ignore()
                else: 
                    response = input('').lower()
                  
            elif direction == "right":
                print('You see some crowd on the far side of the street')
                print('Do you want to go and check what is the deal?')
                self.response2= input('Yes, no ==>>>')
                self.action = False
                answer = 'correct'
                return self.action, self.response2

            elif direction == "forward":
                print('There is a news stand in front of you')
                print("""You can see some head lines on todays news paper. it is not clear\n
                it looks blury you think it have something to do with these empty streets...hummmm?
                \n 0) Do you want to get closer and read it? \n 1) Do you ignore it? """)
                self.response3= input('help/ignore ==>>>')
                self.action = False
                answer = 'correct'
                return self.action, self.response3
            
            else:
                print('Please pick a valid entry')
                direction = input('').lower()
                continue

    def action_help(self):
        print('Geat choice do you want to \nget a ladder  \nclimb the tree?')
        response = input('climb/Ladder ==>>').lower()
        if response == 'climb':
            self.action_climb()
        elif response == 'ladder':
            self.action_ladder()
        else:
            response = input('climb/Ladder ==>>').lower()
            self.action_help()
             

    def action_climb(self):
        print('Can you reach the cat \nYes  \nNo ')
        response = input('Yes/No ==>>').lower()
        if response == 'yes':
            self.option_color()
        elif response == 'no':
            self.action_not_reached()
        else:
            response = input('Yes/No ==>>').lower()
            self.action_climb()

    def action_not_reached(self):
        print('Do you want to get a ladder or go on with your business. ')
        response = input('Ladder/Go ==>>').lower()
        if response == 'ladder':
            self.option_ladder()
        elif response == 'go':
            print("You are back in front of your house on the street....  ")
            print("Where do you want to go:\n>right \n^forward")
            direction = input('').lower()
            if direction == "right" or direction == "forward":
                self.action_directions()
            else: 
                print("Where do you want to go:\n>right \n^forward")
                direction = input('').lower()
        else:
            response = input('ladder/go ==>>').lower()
            self.action_climb()

        print('Great choice do you want to get a ladder or climb the tree?')
        response3 = input('climb /ladder ==>>')

        

    def action_ladder(self):
        print('Oh great you saved a cat that was awsome. Did you notice what color is this cat? \nWhite \nOther ')
        response = input('white/other ==>>').lower()
        if response == 'white':
            print('')
            
        elif response == 'no':
            self.action_ladder()
        else:
            response = input('Yes/No ==>>').lower()
            self.action_climb()
    
    def action_from_left(self):
        print("You are back in front of your house on the street....  ")
        print("Where do you want to go:\n>right \n^forward")
        direction = input('').lower()
        if direction == "right" or direction == "forward":
            self.action_directions()
        else: 
            print("Where do you want to go:\n>right \n^forward")
            direction = input('').lower()
            self.action_from_left()


def play_OutOnStreet():
        outOnStreet = OutOnStreet()
        outOnStreet.on_street()
    


play_OutOnStreet()







