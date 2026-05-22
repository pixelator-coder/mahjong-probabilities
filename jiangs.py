
tile_pool = ["1-wan", "1-wan", "1-wan", "1-wan",
             "2-wan", "2-wan", "2-wan", "2-wan",
             "3-wan", "3-wan", "3-wan", "3-wan",
             "4-wan", "4-wan", "4-wan", "4-wan",
              "5-wan", "5-wan", "5-wan", "5-wan",
             "6-wan", "6-wan", "6-wan", "6-wan",
             "7-wan", "7-wan", "7-wan", "7-wan",
             "8-wan", "8-wan", "8-wan", "8-wan",
             "9-wan", "9-wan", "9-wan", "9-wan",
             "1-tiao", "1-tiao", "1-tiao", "1-tiao",
             "2-tiao", "2-tiao", "2-tiao", "2-tiao",
             "3-tiao", "3-tiao", "3-tiao", "3-tiao",
             "4-tiao", "4-tiao", "4-tiao", "4-tiao",
             "5-tiao", "5-tiao", "5-tiao", "5-tiao",
             "6-tiao", "6-tiao", "6-tiao", "6-tiao",
             "7-tiao", "7-tiao", "7-tiao", "7-tiao",
             "8-tiao", "8-tiao", "8-tiao", "8-tiao",
             "9-tiao", "9-tiao", "9-tiao", "9-tiao",]
hand = []
num_is_jiang = 0
num_possible_hands = 0

def is_jiang(hand):
    num_2wans = hand.count("2-wan")
    num_5wans = hand.count("5-wan")
    num_8wans = hand.count("8-wan")
    num_2tiaos = hand.count("2-tiao")
    num_5tiaos = hand.count("5-tiao")
    num_8tiaos = hand.count("8-tiao")
    if num_2wans >= 2 or num_5wans >= 2 or num_8wans >= 2:
        return True
    if num_2tiaos >= 2 or num_5tiaos >= 2 or num_8tiaos >= 2:
        return True
    return False

for first_tile in tile_pool:
    hand.clear()
    hand.append(first_tile)
    tile_pool1 = tile_pool.copy()
    tile_pool1.remove(first_tile)
    for second_tile in tile_pool1:
        hand.append(second_tile)
        tile_pool2 = tile_pool1.copy()
        tile_pool2.remove(second_tile)
        for third_tile in tile_pool2:
            hand.append(third_tile)
            tile_pool3 = tile_pool2.copy()
            tile_pool3.remove(third_tile)
            for fourth_tile in tile_pool3:
                hand.append(fourth_tile)
                if is_jiang(hand):
                    num_is_jiang += 1
                num_possible_hands += 1
                hand.pop()
            hand.pop()
        hand.pop()

print(num_possible_hands)
print(num_is_jiang)
print(str(100*num_is_jiang/num_possible_hands) + " percent.")