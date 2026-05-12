import random
import math

tile_pool = ["1-wan1", "1-wan2", "1-wan3", "1-wan4",
             "2-wan1", "2-wan2", "2-wan3", "2-wan4",
             "3-wan1", "3-wan2", "3-wan3", "3-wan4",
             "4-wan1", "4-wan2", "4-wan3", "4-wan4",
             "5-wan1", "5-wan2", "5-wan3", "5-wan4",
             "6-wan1", "6-wan2", "6-wan3", "6-wan4",
             "7-wan1", "7-wan2", "7-wan3", "7-wan4",
             "8-wan1", "8-wan2", "8-wan3", "8-wan4",
             "9-wan1", "9-wan2", "9-wan3", "9-wan4",]
hand = set()
num_is_jiang = 0
num_hands = 0

for first_tile in tile_pool:
    new_tile_pool = tile_pool.copy()
    hand.add(first_tile)
    new_tile_pool.remove(first_tile)
    for second_tile in new_tile_pool:
        hand.add(second_tile)
        if "2-wan" in first_tile and "2-wan" in second_tile:
            num_is_jiang += 1
        if "5-wan" in first_tile and "5-wan" in second_tile:
            num_is_jiang += 1
        if "8-wan" in first_tile and "8-wan" in second_tile:
            num_is_jiang += 1
        num_hands += 1
print(num_hands)
print(num_is_jiang)
print(str(100*num_is_jiang/num_hands) + " percent.")