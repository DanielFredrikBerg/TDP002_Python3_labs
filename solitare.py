#!/usr/bin/env python3

from deck import *

#1
d1 = create_deck(True)
shuffle_deck(d1)
#2
joker = card.create_card(0,1)
pos_joker = find_card(d1, joker)
joker = take_card(d1, pos_joker)
if pos_joker == 53:
    insert_card(joker, d1)
else:
    insert_card(joker, d1, pos_joker+1)
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
#4
joker_a = card.create_card(0, 1)
pos_joker_a = find_card(d1, joker_a)

joker_b = card.create_card(0, 2)
pos_joker_b = find_card(d1, joker_b)

if pos_joker_b < pos_joker_a:
    first_joker = pos_joker_b
    second_joker = pos_joker_a
else:
    first_joker = pos_joker_a
    second_joker = pos_joker_b

da = split_deck(d1, first_joker)
second_joker = second_joker - first_joker
first_joker = 0
db = split_deck(d1,second_joker+1)
d1 = cat_decks(d1,db)
d1 = cat_decks(d1,da)

#5
bottem_card = take_card(d1, 53)
move_value = card.get_key_value(bottem_card)
top_part = split_deck(d1, move_value)
d1 = cat_decks(d1, top_part)
insert_card(bottem_card, d1, 53)
