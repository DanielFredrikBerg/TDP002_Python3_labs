#!/usr/bin/env python3

import card

def create_deck():
    deck = ['deck',[]]
    for suit in range(1,5):
        for value in range(1,14):
            deck[1].append(card.create_card(value,suit))
    return deck

def add_jokers(deck):
    for j in range(2):
        deck[1].append(card.create_card(0,0))

def insert_card(card, deck):
    deck[1].append(card)
