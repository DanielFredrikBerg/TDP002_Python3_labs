#!/usr/bin/env python3

from deck import *

#1
d1 = create_deck()
shuffle_deck(d1)
add_jokers(d1)
#2
joker = card.create_card(0,1)
pos_joker = find_card(d1, joker)
joker = take_card(d1, pos_joker)
if pos_joker == 53:
    insert_card(joker, d1)
else:
    insert_card(joker, d1, pos_joker+1)
print(find_card(d1,joker))
#3
joker = card.create_card(0,2)
pos_joker = find_card(d1, joker)
joker = take_card(d1, pos_joker)
if pos_joker == 53:
    insert_card(joker, d1)
elif pos_joker == 52:
    insert_card(joker, d1, 1)
else:
    insert_card(joker, d1, pos_joker+2)
print(find_card(d1,joker))
print(len(d1[1]))
