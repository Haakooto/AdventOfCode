
def solver(input_file):
    score = 0
    card_base = {}
    for line in open(input_file, 'r').read().split("\n")[:-1]:
        id, card = line.split(": ")
        id = int(id.split(" ")[-1])
        winners, haves = card.split(" | ")
        winners = set([int(i) for i in winners.split(" ") if i != ""])
        haves = set([int(i) for i in haves.split(" ") if i != ""])
        overlap = winners.intersection(haves)
        card_base[id] = {"count": 1, "hits": len(overlap)}
        if overlap:
            score += 2**(len(overlap)-1)
        
    for card_id in card_base:
        for i in range(card_base[card_id]["hits"]):
            card_base[card_id + i + 1]["count"] += card_base[card_id]["count"]
    
    return score, sum([v["count"] for v in card_base.values()])

def test_part(input, true, part2=False):
    ans = solver(input)
    ans = ans[1] if part2 else ans[0]
    if ans != true:
        raise Exception(f"Test part 1 failed for {input}. Expected {true}, got {ans}")

def main():
    test1 = "test_input.txt" 
    real = "input.txt"

    test_part(test1, 13)
    p1, p2 = solver(real)
    print(f"Part 1: {p1}")
    
    test_part(test1, 30, part2=True)
    print(f"Part 2: {p2}")
    
if __name__ == "__main__":
    main()
