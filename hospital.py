import time


class Player():
    def __init__(self):
        self.key_fragments = 0

    def add_key(self):
        self.key_fragments += 1


player = Player()


class HospitalRoom():
    def __init__(self):
        self.has_key = False

    def get_key_value(self):
        return self.has_key

    def set_key_found(self):
        self.has_key = True

    def room_start(self):
        print('As you step through the door you are met with blindingly white light...')
        time.sleep(1)
        print('After taking a few steps into the room your eyes begin to adjust.')
        time.sleep(1)
        print('You find yourself in what seems to be an operating room in some kind of hospital.')
        time.sleep(1)
        print(
            'As you survey the room you notice to your left there is a large storage unit,')
        time.sleep(1)
        print(
            'toward the middle of the room the hospital bed is pushed up against the wall.')
        time.sleep(1)
        print('The bed seems to house a person under the sheets but they are pulled up well above the individuals head.')
        time.sleep(1)
        print('As you continue to scan the room the last thing you notice to the right is a what looks like a large window covered by a curtain.')
        time.sleep(1)
        print('When you look behind you, the door you came through is no longer there. Looks like you\'ll have to explore the room to find a way out.')
        time.sleep(1)

    def main_room_view(self):
        print('Standing where the door used to be, which would you like to explore? Enter left/center/right')
        choice_main = input().lower()
        if choice_main == 'left':
            print(
                'You choose to explore the storage unit to see if you can figure out why you are here.')
            time.sleep(1)
            self.left_room_view()
        elif choice_main == 'center':
            print(
                'You feel drawn to the bed in the center of the room and the figure hidden under the sheets.')
            self.center_room_view()
            time.sleep(1)
        elif choice_main == 'right':
            print(
                'The window to the right looks like it could tell you more about where you are.')
            time.sleep(1)
        else:
            print('That command did nothing, try entering left/center/right to progress.')

    def left_room_view(self):
        print('You approach the storage unit and realize it seems to be made up of sections including cabinets and file storage.')
        time.sleep(1)
        print('Which would you like to investigate? cabinet/files')
        choice_left = input().lower()
        if choice_left == 'cabinet':
            self.cabinets()
        elif choice_left == 'files':
            self.files()
        else:
            print('That command did nothing, try entering left/center/right to progress.')

    def cabinets(self):
        print('You begin opening the cabinets and searchong for anything that might be useful.')
        time.sleep(1)
        print('Most of the cabinets are either empty or house supplies such as gauze, tape, and sterilization wipes.')
        time.sleep(1)
        print('These dont seem very helpful for your current situation but you keep them in mind in case the become useful.')
        time.sleep(1)
        print('What is your next move? Check out the files or go back? files/back')
        choice_cabinet = input().lower()
        if choice_cabinet == 'files':
            self.files()
        elif choice_cabinet == 'back':
            self.main_room_view()
        else:
            print('That command did nothing, try entering left/center/right to progress.')

    def files(self):
        print('You move on to investigate the filing cabinet next to you. The drawers are full of files and papers,')
        time.sleep(1)
        print('but all of them are printed REDACTED and have most of the information blocked out. As you sift through the stacks of paper,')
        time.sleep(1)
        print('the words you can read seem to trigger a feeling of familiarity as you scan them but you cannot place why.')
        time.sleep(1)
        print('It looks like there is nothing this section that can help you right now.')
        time.sleep(1)
        print('Would you like to keep exploring the cabinets or go back? cabinets/back')
        choice_files = input().lower()
        if choice_files == 'cabinets':
            self.cabinets()
        elif choice_files == 'back':
            self.main_room_view()

    def center_room_view(self):
        print('Standing in the center of the room, you observe your options.')
        time.sleep(1)
        print('To your left, the stack of screens and monitors flickers gently. For the first time you notice,')
        time.sleep(1)
        print('to your right there is a bathroom that was hidden out of view initially.')
        time.sleep(1)
        print('Where do you want to investigate? bed/screens/bathroom')
        choice_center = input().lower()
        if choice_center == 'bed':
            self.bed()
        elif choice_center == 'screens':
            self.screens()
        elif choice_center == 'bathroom':
            self.bathroom()
        else:
            print('That command did nothing, try entering left/center/right to progress.')

    def bed(self):
        print('You move closer to the bed and from this distance you are sure there is someone or something under the sheets.')
        time.sleep(1)
        print('Do you move the sheet or back away? continue/back')
        choice_bed = input().lower()
        if choice_bed == 'continue':
            print(
                'You reach out and begin to move the sheet away from the top of the bed.')
            time.sleep(1)
            print('As you pull farther you tense and prepare yourself for what youre about to see as you pass where the figures head should be...')
            time.sleep(3)
            print('...nothing. The bed is empty as if there was never anything there in the first place, but you could swear there was...')
            time.sleep(1)
            print(
                'Nothing seems to be changing about the bed so you have a few more options to investigate.')
            time.sleep(1)
            print(
                'Would you like to observe the screens for more clues or go back? screens/back')
            choice_after_bed = input().lower()
            if choice_after_bed == 'screens':
                self.screens()
            elif choice_after_bed == 'back':
                self.center_room_view()
            else:
                print(
                    'That command did nothing, try entering left/center/right to progress.')

    def screens(self):
        print('You turn toward the screens used to monitor vitals and status.')
        time.sleep(1)
        print('Looking at the screens you notice a faint deviation in the line indicating a pulse...')
        time.sleep(1)
        print('This furthers your suspicions that something is very wrong about this room you are in.')
        time.sleep(1)
        print('You shake off your feeling and tell yourself you should keep exploring to find your way out. Enter back to go back')
        choice_screens = input().lower()
        if choice_screens == 'back':
            self.center_room_view()
        else:
            print('That command did nothing, try entering left/center/right to progress.')

    def bathroom(self):
        print('As you enter the bathroom and evaluate your surroundings you notice you are a few steps out of view of the mirror,')
        time.sleep(3)
        print('and to your left you notice a small trash can with something sticking out of the top as if haphazardly tossed in.')
        time.sleep(3)
        print('Would you like to step farther into the room and check the mirror or investigate the trash? mirror/trash')
        choice_bathroom = input().lower()
        if choice_bathroom == 'mirror':
            self.mirror()
        elif choice_bathroom == 'trash':
            self.trash()
        else:
            print('That command did nothing, try entering left/center/right to progress.')

    def mirror(self):
        print('For some reason you feel a strong urge to fully enter the room and turn to look in the mirror.')
        time.sleep(3)
        print('As you turn to look in the mirror you find you are met with a clear view of the bathrom wall behind you and nothing else.')
        time.sleep(3)
        print('Your stomach lurches and you slowly raise a hand to check your own sanity. The hand in front of you looks as real as ever,')
        time.sleep(3)
        print('yet the mirror still shows an empty room. You panic and scramble back out ov view of the mirror.')
        time.sleep(3)
        print('As your heartbeat slows you contemplate if you would like to keep exploring the bathroom or go back. continue/back')
        choice_mirror = input().lower()
        if choice_mirror == 'continue':
            self.trash()
        elif choice_mirror == 'back':
            self.main_room_view()
        else:
            print('That command did nothing, try entering left/center/right to progress.')

    def trash(self):
        print('You approach the trash and inspect what seems to be a file similar to those in the storage unit that has been thrown away.')
        time.sleep(3)
        print('Should you take the file out of the trash? yes/no')
        choice_trash = input().lower()
        if choice_trash == 'yes':
            print(
                'You bend down and remove the file from the trash to further inspect it.')
            time.sleep(3)
            print('You begin to flip through the file and this time you can make out the name fairly well. You still do not recognize the information fully,')
            time.sleep(3)
            print('but something about it seems to click in your mind in a familiar way.')
            time.sleep(3)
            print('As you flip further into the file something slides from between the pages and falls to the ground.')
            time.sleep(3)
            print('You look down and find an object on the ground that seems to roughly resemble a broken piece of what looks to be some sort of key.')
            time.sleep(3)
            print('Do you pick up the key fragment? yes/no')
            choice_key = input().lower()
            if choice_key == 'yes':
                self.exit_room()
            elif choice_key == 'no':
                self.main_room_view()
            else:
                print(
                    'That command did nothing, try entering left/center/right to progress.')
        elif choice_trash == 'no':
            self.main_room_view()
        else:
            print('That command did nothing, try entering left/center/right to progress.')

    def exit_room(self):
        print('You bend down to pick up the key, as your fingers touch the key a bright light envelops your vision,')
        time.sleep(3)
        print('and you feel yourself closing your eyes as everything fades to black.')
        return


hospital_key = False


def play_hospital_room():
    hospital_room = HospitalRoom()
    print(hospital_key)

    if hospital_key == False:
        hospital_room.room_start()
        hospital_room.main_room_view()
        hospital_key = True
        print(hospital_key)
        player.add_key()
        print(player.key_fragments)
    elif hospital_key == True:
        print('This room seems to be locked now, try another room.')
        return


play_hospital_room()
