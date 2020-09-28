#!/usr/bin/env python3

from deck import *
import sys
#letters = {
#    1 : 'A',
#    2 : 'B',
#    3 : 'C',
#    4 : 'D',
#    5 : 'E',
#    6 : 'F',
#    7 : 'G',
#    8 : 'H',
#    9 : 'I',
#    10: 'J',
#    11: 'K',
#    12: 'L',
#    13: 'M',
#    14: 'N',
#    15: 'O',
#    16: 'P',
#    17: 'Q',
#    18: 'R',
#    19: 'S',
#    20: 'T',
#    21: 'U',
#    22: 'V',
#    23: 'W',
#    24: 'X',
#    25: 'Y',
#    26: 'Z',
#    27: ''
#}

#1
def solitaire_keystream(length, deck):
    keystream = ''
    while(len(keystream) < length):
        #2
        joker = card.create_card(27,1)
        pos_joker = find_index(deck, joker)
        joker = take_card(deck, pos_joker)
        if pos_joker == 27:
            insert_card(joker, deck, 1)
        else:
            insert_card(joker, deck, pos_joker+1)
        #3
        joker = card.create_card(27,2)
        pos_joker = find_index(deck, joker)
        joker = take_card(deck, pos_joker)
        if pos_joker == 27:
            insert_card(joker, deck, 2)
        elif pos_joker == 26:
            insert_card(joker, deck, 1)
        else:
            insert_card(joker, deck, pos_joker+2)
        #4
        joker_a = card.create_card(27, 1)
        pos_joker_a = find_index(deck, joker_a)

        joker_b = card.create_card(27, 2)
        pos_joker_b = find_index(deck, joker_b)

        if pos_joker_b < pos_joker_a:
            first_joker = pos_joker_b
            second_joker = pos_joker_a
        else:
            first_joker = pos_joker_a
            second_joker = pos_joker_b

        da = split_deck(deck, first_joker)
        second_joker = second_joker - first_joker
        db = split_deck(deck,second_joker+1)
        deck = cat_decks(deck,db)
        deck = cat_decks(deck,da)

        #5
        bottom_card = take_card(deck, find_bottom_index(deck))
        move_value = card.get_key_value(bottom_card)
        top_part = split_deck(deck, move_value)
        deck = cat_decks(deck, top_part)
        insert_card(bottom_card, deck, find_bottom_index(deck))

        #6
        top_card = pick_card(deck)
        top_card_value = card.get_key_value(top_card)
        chosen_card = pick_card(deck, top_card_value - 1)
        chosen_card_value = card.get_key_value(chosen_card)
        letter = chr(chosen_card_value + 64)
        keystream = keystream + letter
#        print (keystream)
#        print(len(keystream))
    return keystream

def ints_to_string(nums):
    word = ''
    for num in nums:
        word += chr(num+64)
    return word

def string_to_ints(word):
    nums = list()
    for letter in word:
        nums.append(ord(letter)-64)
    return nums

def solitaire_encrypt(word, deck):
    #1
    word = word.upper()
    whitelist = set ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    word = "".join(filter(whitelist.__contains__, word))
    #2
    length_of_word = len(word)
    keystream = solitaire_keystream(length_of_word, deck)
    #3
    nums = string_to_ints(word)
    #4
    keynums = string_to_ints(keystream)
#    print(keystream, word)
#    print(keynums, nums)
    #5
    for i in range(len(nums)):
        nums[i] += keynums[i]
        if nums[i] > 26:
            nums[i] = nums[i]%26
    #6
    enc_word = ints_to_string(nums)
    return enc_word


def solitaire_decrypt(enc_word, deck):
    enc_word = enc_word.upper()
    #1
    enc_nums = string_to_ints(enc_word)
    #2
    keystream = solitaire_keystream(len(enc_word), deck)
    #3
    keynums = string_to_ints(keystream)
    #4
    for i in range(len(enc_nums)):
        enc_nums[i] -= keynums[i]
        if enc_nums[i] < 1:
            enc_nums[i] = enc_nums[i] + 26
    #5
    word = ints_to_string(enc_nums)
    return word

#print(solitaire_decrypt(enc_word, sd2))
def main():
    if len(sys.argv) < 4:
        print("Write a flag [-e, -d], a seed[INT] and word[STRING]")
    else:
        if sys.argv[1] == '-e':
            sd1 = create_solitaire_deck(int(sys.argv[2]))
            encrypted_word = solitaire_encrypt(str(sys.argv[3]), sd1)
            print("Encrypted word: " + encrypted_word)
        elif sys.argv[1] == "-d":
            sd2 = create_solitaire_deck(int(sys.argv[2]))
            decrypted_word = solitaire_decrypt(str(sys.argv[3]), sd2)
            print("Decrypted word: " + decrypted_word)
        else:
            print("Valid flags: -d, -e")
if __name__ =="__main__":
    main()
