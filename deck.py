#!/usr/bin/env python3

import card
import random

def create_deck():
    deck = ['deck',[]]
    for suit in range(1,5):
        for value in range(1,14):
            deck[1].append(card.create_card(value,suit))
    return deck

def add_jokers(deck):
    for j in range(2):
        deck[1].append(card.create_card(0,j+1))

def find_card(deck, value, suit):
    i = 0
    for card in deck[1]:
        if card == (value, suit):
            return i
        i += 1

def split_deck(deck, position):
    for i in range(position):
        move_card(0, len(deck[1]), deck)
    return deck

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
