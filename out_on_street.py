# You are wlking down the street it looks just like the one out of your door
# feeling 
import time

class OutOnStreet():

    def __init__(self):
            self.has_key = False
    
    def set_key_found(self):
            self.has_key = True

    def on_street(self):

        print("You are out of your house walking on the street it is sunny and warm. The street looks quite you are the only one walking around....  ")
        print("Where do you want to go: \n<left \n>right \n^forward")
        direction = input('').lower()
    
        answer = 'incorrect'

        while answer == 'incorrect':

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
        print('Geat choice do you want to \nget a ladder  \nclimp the tree?')
        response = input('Climp/Ladder ==>>').lower()
        if response == 'climp':
            self.action_climp()
        elif response == 'ladder':
            self.action_ladder()
        else:
            response = input('Climp/Ladder ==>>').lower()
            self.action_help()
             

    def action_climp(self):
        print('Can you reach the cat \nYes  \nNo ')
        response = input('Yes/No ==>>').lower()
        if response == 'yes':
            self.option_color()
        elif response == 'no':
            self.action_ladder()
        else:
            response = input('Yes/No ==>>').lower()
            self.action_climp()

        print('Geat choice do you want to get a ladder or climp the tree?')
        response3 = input('climp /ladder ==>>')

        

    def action3(self):
        if self.action3 == True:
            print('This is action 3')
            actions2= True
        else:
            actions2 = False
            print('you picked yes')
            return actions2

        print('Geat choice do you want to get a ladder or climp the tree?')
        response3 = input('climp /ladder ==>>')

        if self.action == True:
            print('yes it is true')
            actions2= True
        else:
             actions2 = False
        return actions2

def play_OutOnStreet():
        outOnStreet = OutOnStreet()
        outOnStreet.on_street()
    


play_OutOnStreet()







