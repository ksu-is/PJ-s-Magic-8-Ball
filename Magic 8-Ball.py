# This is where the code is going to be.
# W.I.P
import random
import time

responses = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Do not count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."]


def play_game():
    inp = input('What would you like to ask the mighty magic 8 ball? ')
    print("You asked: '" + str(inp) + "'")
    time.sleep(1)
    print("Let me see... ")
    time.sleep(1.25) 