#!/usr/bin/env python3
def __get_possible_values__():
    return {
    1 : 'Ace',
    2 : 'Two',
    3 : 'Three',
    4 : 'Four',
    5 : 'Five',
    6 : 'Six',
    7 : 'seven',
    8 : 'Eight',
    9 : 'Nine',
    10: 'Ten',
    11: 'Jack',
    12: 'Queen',
    13: 'King'
    }

def return_value(value):
    possible_values = __get_possible_values__()
    return possible_values[value]

def __get_possible_suits__():
    return  {
    1 : 'Hearts',
    2 : 'Spades',
    3 : 'Diamonds',
    4 : 'Clovers'
    }

def return_suit(suit):
    possible_suits = __get_possible_suits__()
    return possible_suits[suit]

def create_card(value, suit):
    if value == 0:
        card = 'Joker'
    else:
        #Fix alla metoder efter nummeriska tupler nedan
        card = (value, suit)
    return card

def display_card(card):
    if card == 'Joker':
        print('Joker')
    else:
        print(card[0] + " of " + card[1])
