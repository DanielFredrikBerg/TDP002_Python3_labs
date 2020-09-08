#!/usr/bin/env python3
def get_value(value):
    values = {
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
        13: 'King',
        14: 'Ace',
        15: 'Two',
        16: 'Three',
        17: 'Four',
        18: 'Five',
        19: 'Six',
        20: 'seven',
        21: 'Eight',
        22: 'Nine',
        23: 'Ten',
        24: 'Jack',
        25: 'Queen',
        26: 'King',
        27: 'Joker'
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
#    if value == 0:
#        card = (0,0)
#    else:
        #Fix alla metoder efter nummeriska tupler nedan
    card = (value, suit)
    return card

#def display_card(card):
#    if card[0] == 0:
#        print("Joker")
#    else:
#        print(get_value(card[0]) + " of " + get_suit(card[1]))

def display_card(card):
    if card[0] == 27:
        print("Joker")
    elif card[0] > 13:
        print(get_value(card[0]) + " of " + get_suit(2))
    else:
        print(get_value(card[0]) + " of " + get_suit(1))


def get_key_value(card):
    return card[0]

def get_key_suit(card):
    return card[1]
