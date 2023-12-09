from collections import Counter

class Card_p1:
    pic_to_num = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14} 
    pic_to_num = {**pic_to_num, **{str(i): i for i in range(2, 10)}} 

    def __init__(self, hand: str, bid: int):
        self.hand = hand
        self.bid = bid
        self.type = self.type_val()

    def type_val(self):
        counts = list(Counter(self.hand).values())
        signature = {(5,): 7,  # five of a kind
                     (1, 4): 6, # four of a kind
                     (2, 3): 5, # full house
                     (1, 1, 3): 4, # three of a kind
                     (1, 2, 2): 3, # two pairs
                     (1, 1, 1, 2): 2, # one pair
                     (1, 1, 1, 1, 1): 1} # high card
        return signature[tuple(sorted(counts))]
    
    def num_compare(self, other):
        for i in range(len(self.hand)):
            mynum = self.pic_to_num[self.hand[i]]
            othernum = self.pic_to_num[other.hand[i]]
            if mynum != othernum:
                return mynum < othernum
    
    def __lt__(self, other):
        if self.type != other.type:
            return self.type < other.type
        return self.num_compare(other)
    
    def __repr__(self):
        return f"{self.hand}"
    
class Card_p2(Card_p1):
    pic_to_num = {**Card_p1.pic_to_num, **{"J": 1}}
    
    def type_val(self):
        counts = Counter(self.hand)
        Js = counts["J"]
        if Js in (4, 5):
            return 7  # five of a kind
        elif Js == 3:
            if len(counts) == 2:
                return 7  # five of a kind
            return 6 # four of a kind
        elif Js == 2:
            if len(counts) == 4:
                return 4  # three of a kind
            if len(counts) == 3:
                return 6 # four of a kind
            return 7  # five of a kind
        elif Js == 1:
            if len(counts) == 2:
                return 7 # five of a kind
            if len(counts) == 3:
                if 3 in counts.values():
                    return 6 # four of a kind
                return 5 # full house
            if len(counts) == 4:
                return 4 # three of a kind
            return 2 # one pair
        return super().type_val()
        

def solver(input_file, part2=False):
    if part2:
        Card = Card_p2
    else:
        Card = Card_p1
    cards = []

    for line in open(input_file).read().split("\n")[:-1]:
        hand, bid = line.split(" ")
        cards.append(Card(hand, int(bid)))

    cards = sorted(cards)
    winnings = 0
    for i, card in enumerate(cards):
        winnings += card.bid * (i + 1)
    
    return winnings

