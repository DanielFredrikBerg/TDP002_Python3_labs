#!/usr/bin/env python3

from deck import *
#solitaire keystream begin
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
sd1 = create_solitaire_deck(10)
sd2 = create_solitaire_deck(10)
#Sorry
def solitaire_keystream(length = 30, sd1 = sd1):
    keystream = ''
    while(len(keystream) < length):
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
        bottom_card = take_card(sd1, len(sd1[1])-1)
        move_value = card.get_key_value(bottom_card)
        top_part = split_deck(sd1, move_value)
        sd1 = cat_decks(sd1, top_part)
        insert_card(bottom_card, sd1, len(sd1[1])-1)

        #6
        top_card = pick_card(sd1, 0)
        top_card_value = card.get_key_value(top_card)
        chosen_card = pick_card(sd1, top_card_value+1)
        chosen_card_value = card.get_key_value(chosen_card)
        letter = letters[chosen_card_value]
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
    #Check wtf this does.
    word = "".join(filter(whitelist.__contains__, word))
    #2
    length_of_word = len(word)
    keystream = solitaire_keystream(length_of_word, deck)
    #3
    nums = string_to_ints(word)
    #4
    keynums = string_to_ints(keystream)
    print(keystream, word)
    print(keynums, nums)
    #5
    for i in range(len(nums)):
        nums[i] += keynums[i]
        if nums[i] > 26:
            nums[i] = nums[i]%26
    #6
    enc_word = ints_to_string(nums)
    return enc_word

enc_word = solitaire_encrypt("AdijfvjmfoiIO2348972()(8z9/)HEHEHE", sd1)

def solitaire_decrypt(enc_word, deck = sd2):
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

print(solitaire_decrypt(enc_word, sd2))
