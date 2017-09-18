#!/usr/bin/env python
'''Build a working roulette game.  At minimum, this script should
Complete one round of roulette - but if you're up to the challenge,
feel free to build a full command line interface through which '''

import random
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

bank_account = 1000
bet_amount = 0
bet_color = None
bet_number = None

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

def take_bet(color, number, amount):
    bet_color = color
    bet_number = number
    bet_amount = amount
    return [bet_color, bet_number, bet_amount]
def roll_ball():
    '''returns a random number between 0 and 37'''
    # and also check for which color group the number is in
    x = random.randint(0, 38)
    if x in green:
        return [x,"green"]
    elif x in red:
        return [x,"red"]
    else:
        return [x,"black"]
    return x

roll_ball()

def check_results(rolled_ball, rolled_color, player_bet):
    '''Compares bet_color to color rolled.  Compares
    bet_number to number_rolled.'''
    print("the num randomly rolled", int(rolled_ball))

    if rolled_ball == player_bet[1]:
        won_number = "check number"
        payout(won_number, player_bet)
    elif rolled_color == player_bet[0]:
        won_number = "check color"
        payout(won_number, player_bet)
    else:
        print("you failed")
        won_number = None
        payout(won_number, player_bet)
    pass

def payout(won_number, player_bet):
    if won_number == "check number":
        print("Congrats, you won ", str(bank_account + player_bet[2]))
    elif won_number == "check color":
        print("Congrats, you won a little ", str(bank_account + 0.5 * player_bet[2]))
    else:
        print("Sorry, you lose ", str(bank_account - player_bet[2]))
    '''returns total amount won or lost by user based on results of roll. '''
    pass

def play_game():
    """This is the main function for the game.
    When this function is called, one full iteration of roulette,
    including:
    Take the user's bet.
    Roll the ball.
    Determine if the user won or lost.
    Pay or deduct money from the user accordingly.
    """
    ask_mood = input("Do you wanna pick number or color?")
    if ask_mood = "color":
        # user pick color
        color = input("choose color\t")
    elif ask_mood = "number":
        number = input("choose a number from 2-36\t")
            if number in green:
                color = "green"
                play_game()
            elif number in red:
                color = "red"
            else:
                color = "black"
    check_results(roll_ball()[0], roll_ball()[1], take_bet(color, number, int(input("how much do you wanna bet?\t"))))
    pass
play_game()


