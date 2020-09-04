#!/usr/bin/env python3

import card
import random

#is broken, pls fix
#cant insert, out of bounds
def create_deck(add_jokers = False):
    deck = ['deck',[]]
    for suit in range(1,5):
        for value in range(1,14):
#            deck[1].append(card.create_card(value,suit))
            insert_card(card.create_card(value,suit), deck[1])
    if add_jokers:
        for i in range(2):
            insert_card(card.create(0,i+1), deck[1])
    return deck

#def add_jokers(deck):
#    for j in range(2):
#        deck[1].append(card.create_card(0,j+1))

def find_card(deck, card):
    return deck[1].index(card)

def split_deck(deck, position):
    deck_slice = ['deck',[]]
    for i in range(position):
        insert_card(take_card(deck, 0),deck_slice)
    return deck_slice[1].reverse()

def insert_card(card, deck, pos = 0):
    deck[1].insert(pos, card)

def pick_card(deck):
    return deck[1][0]

def take_card(deck, pos):
    card = deck[1][pos]
    deck[1].pop(pos)
    return card

def shuffle_deck(deck):
    random.shuffle(deck[1])

def move_card(pos1, pos2, deck):
    card = take_card(deck, pos1)
    insert_card(card, deck, pos2)
