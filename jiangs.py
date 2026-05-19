import random
import math

tile_pool = ["1-wan", "1-wan", "1-wan", "1-wan",
             "2-wan", "2-wan", "2-wan", "2-wan",
             "3-wan", "3-wan", "3-wan", "3-wan",
             "4-wan", "4-wan", "4-wan", "4-wan",
             "5-wan", "5-wan", "5-wan", "5-wan",
             "6-wan", "6-wan", "6-wan", "6-wan",
             "7-wan", "7-wan", "7-wan", "7-wan",
             "8-wan", "8-wan", "8-wan", "8-wan",
             "9-wan", "9-wan", "9-wan", "9-wan",]
hand = []
num_is_jiang = 0
num_possible_hands = 0

def is_jiang(hand):
    num_2s = hand.count("2-wan")
    num_5s = hand.count("5-wan")
    num_8s = hand.count("8-wan")
    if num_2s >= 2 or num_5s >= 2 or num_8s >= 2:
        return True
    return False

for first_tile in tile_pool:
    hand.clear()
    new_tile_pool = tile_pool.copy()
    hand.append(first_tile)
    new_tile_pool.remove(first_tile)
    for second_tile in new_tile_pool:
        hand.append(second_tile)
        if is_jiang(hand):
            num_is_jiang += 1
        num_possible_hands += 1
        hand.pop(1)

print(num_possible_hands)
print(num_is_jiang)
print(str(100*num_is_jiang/num_possible_hands) + " percent.")