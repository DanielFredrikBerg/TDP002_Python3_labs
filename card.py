#!/usr/bin/env python3
def get_value(value):
    values = {
        0 : 'Joker',
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
    return values[value]

#def return_value(value):
#    possible_values = __get_possible_values__()
#    return possible_values[value]

def get_suit(select):
    suits = {
        1 : 'Hearts',
        2 : 'Spades',
        3 : 'Diamonds',
        4 : 'Clovers'
    }
    return suits[select]

#def return_suit(suit):
#    possible_suits = __get_possible_suits__()
#    return possible_suits[suit]

def create_card(value, suit):
    if value == 0:
        card = (0,0)
    else:
        #Fix alla metoder efter nummeriska tupler nedan
        card = (value, suit)
    return card

def display_card(card):
    if card[0] == 0:
        print("Joker")
    else:
        print(return_value(card[0]) + " of " + return_suit(card[1]))
