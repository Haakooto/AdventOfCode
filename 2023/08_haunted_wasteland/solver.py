from math import lcm

def solver(input_file, part2=False):
    with open(input_file, "r") as f:
        LRs, postions = f.read().split("\n\n")
    if part2:
        start = "A"
        end = "Z"
        match = lambda x: x[-1]
    else:
        start = "AAA"
        end = "ZZZ"
        match = lambda x: x
    LRs = [0 if i == "L" else 1 for i in LRs]
    postions = postions.split("\n")[:-1]
    maps = {}
    As = []
    for map in postions:
        p, t = map.split(" = ")
        a, b = t[1:-1].split(", ")
        maps[p] = [a, b]
        if match(p) == start:
            As.append(p)
    turns = []
    for current in As:
        turn = 0
        while match(current) != end:
            instr = LRs[turn % len(LRs)]
            current = maps[current][instr]
            turn += 1
        turns.append(turn)
    return lcm(*turns)

def test_part(input, true, part2=False):
    ans = solver(input, part2=part2)

    if ans != true:
        raise Exception(f"Test part {'2' if part2 else '1'} failed for {input}. Expected {true}, got {ans}")

def main():
    test1 = "test_input.txt" 
    test2 = "test_input_2.txt" # Update this if two test inputs
    test3 = "test_input_3.txt" # Update this if two test inputs
    real = "input.txt"
    
    test_part(test1, 2)
    test_part(test2, 6)
    print(f"Part 1: {solver(real)}")
    test_part(test3, 6, part2=True)
    print(f"Part 2: {solver(real, part2=True)}")
    
if __name__ == "__main__":
    main()
