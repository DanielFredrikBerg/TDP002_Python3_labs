#!/usr/bin/env python3

from deck import *
#solitare keystream begin
letters = {
    1 : 'A',
    2 : 'B',
    3 : 'C',
    4 : 'D',
    5 : 'E',
    6 : 'F',
    7 : 'G',
    8 : 'H',
    9 : 'I',
    10: 'J',
    11: 'K',
    12: 'L',
    13: 'M',
    14: 'N',
    15: 'O',
    16: 'P',
    17: 'Q',
    18: 'R',
    19: 'S',
    20: 'T',
    21: 'U',
    22: 'V',
    23: 'W',
    24: 'X',
    25: 'Y',
    26: 'Z',
    27: ''
}

#1
sd1 = create_solitare_deck()
shuffle_deck(sd1)
#2
joker = card.create_card(27,1)
pos_joker = find_card(sd1, joker)
joker = take_card(sd1, pos_joker)
if pos_joker == 27:
    insert_card(joker, sd1)
else:
    insert_card(joker, sd1, pos_joker+1)
#3
joker = card.create_card(27,2)
pos_joker = find_card(sd1, joker)
joker = take_card(sd1, pos_joker)
if pos_joker == 27:
    insert_card(joker, sd1)
elif pos_joker == 26:
    insert_card(joker, sd1, 1)
else:
    insert_card(joker, sd1, pos_joker+2)
#4
joker_a = card.create_card(27, 1)
pos_joker_a = find_card(sd1, joker_a)

joker_b = card.create_card(27, 2)
pos_joker_b = find_card(sd1, joker_b)

if pos_joker_b < pos_joker_a:
    first_joker = pos_joker_b
    second_joker = pos_joker_a
else:
    first_joker = pos_joker_a
    second_joker = pos_joker_b

da = split_deck(sd1, first_joker)
second_joker = second_joker - first_joker
first_joker = 0
db = split_deck(sd1,second_joker+1)
sd1 = cat_decks(sd1,db)
sd1 = cat_decks(sd1,da)

#5
bottem_card = take_card(sd1, 27)
move_value = card.get_key_value(bottem_card)
top_part = split_deck(sd1, move_value)
sd1 = cat_decks(sd1, top_part)
insert_card(bottem_card, sd1, 27)

#6
top_card = pick_card(sd1, 0)
top_card_value = card.get_key_value(top_card)
if top_card_value > 26:
    print(top_card)
    print("joker :P")
else:
    chosen_card = take_card(sd1, top_card_value+1)
    print(chosen_card)
    chosen_card_value = card.get_key_value(chosen_card)
    letter = letters[chosen_card_value]
    print(sd1, end='')
    print(letter)
