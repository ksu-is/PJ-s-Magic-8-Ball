# This is where the code is going to be.
import random
import time


responses = [
    "Fasho",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "For real for real.",
    "Outlook good.",
    "Yes.",
    "Thats the way it is.",
    "Reply hazy, try again.",
    "Ask again later.",
    "you know it!",
    "Do not count on it.",
    "My reply is no.",
    " No way loser.",
    "Outlook not so good.",
    "Very doubtful."]


def play_game():
    inp = input('What you need from me, the magic 8 ball? ')
    print("You asked: '" + str(inp) + "'")
    time.sleep(.5)
    print("Let me see... ")
    time.sleep(1.25) 
    print("...Still thinking... ")
    time.sleep(2)
    print("...Sorry got distracted... ")
    time.sleep(1.5)
    print("...Aha, got it... ")
    time.sleep(2)
    print(responses[random.randint(0, len(responses) - 1)])
    play_again()  

def play_again():
    quest = input("What else you want from me fool? ")
    if quest == 'yes':
        print('')
        play_game()
    elif quest != 'yes':
        print('')
        time.sleep(1.5)
        print('...Later bro! ...')
        quit()

play_game()
