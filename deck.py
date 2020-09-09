#!/usr/bin/env python3

import card
import random

#def create_deck(add_jokers = False):
#    deck = ['deck',[]]
#    for suit in range(1,5):
#        for value in range(1,14):
#            insert_card(card.create_card(value,suit), deck)
#    if add_jokers:
#        for i in range(2):
#            insert_card(card.create_card(0,i+1), deck)
#    return deck
def create_solitaire_deck(seed):
    random.seed(seed)
    deck = ['deck', []]
    suit = 1;
    for value in range(1,27):
        if value > 13:
            suit = 2
        insert_card(card.create_card(value,suit), deck)
    for i in range(2):
        insert_card(card.create_card(27, i+1), deck)
    shuffle_deck(deck)
    return deck

def find_index(deck, card):
    return deck[1].index(card)

def find_bottom_index(deck):
    return len(deck[1])-1

def split_deck(deck, position):
    deck_slice = ['deck',[]]
    for i in range(position):
        insert_card(take_card(deck, 0),deck_slice)
    deck_slice[1].reverse()
    return deck_slice

def insert_card(card, deck, pos = 0):
    deck[1].insert(pos, card)

def pick_card(deck, pos = 0):
    return deck[1][pos]

def take_card(deck, pos):
    card = deck[1][pos]
    deck[1].pop(pos)
    return card

def shuffle_deck(deck):
    random.shuffle(deck[1])

def move_card(pos1, pos2, deck):
    card = take_card(deck, pos1)
    insert_card(card, deck, pos2)

def cat_decks(deck1, deck2):
    deck = ['deck',[]]
    deck[1] = deck1[1] + deck2[1]
    return deck
