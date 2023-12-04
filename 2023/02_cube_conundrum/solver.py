
def solver(input_file):
    possible = 0
    power = 0
    for line in open(input_file, 'r').read().split("\n")[:-1]:
        id, game = line.split(": ")
        id = id.split(" ")[1]
        maxes = {"red": 0, "green": 0, "blue": 0}
        for turn in game.split("; "):
            for cube in turn.split(", "):
                count, color = cube.split(" ")
                maxes[color] = max(maxes[color], int(count))
        power += maxes["red"] * maxes["green"] * maxes["blue"]
        if maxes["red"] > 12 or maxes["green"] > 13 or maxes["blue"] > 14:
            continue
        possible += int(id)
    return possible, power

def test_parts(input, true, part2=False):
    ans = solver(input)
    ans = ans[1] if part2 else ans[0]
    if ans != true:
        raise Exception(f"Test part {'2' if part2 else '1'} failed for {input}. Expected {true}, got {ans}")

def main():
    test = "test_input.txt" 
    real = "input.txt"

    test_parts(test, 8)
    test_parts(test, 2286, part2=True)
    
    p1, p2 = solver(real)
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
    
if __name__ == "__main__":
    main()
