
def extrapolate(seq):
    diffs = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
    if set(diffs) == {0}:
        return seq[-1] + diffs[-1]
    else:
        new = extrapolate(diffs)
        return seq[-1] + new

def baxtrapolate(seq):
    diffs = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
    if set(diffs) == {0}:
        return seq[0] - diffs[0]
    else:
        new = baxtrapolate(diffs)
        return seq[0] - new
    
def solver1(input_file):
    ans = 0
    for line in open(input_file, "r").read().split("\n")[:-1]:
        sequence = [int(i) for i in line.split(" ")]
        ans += extrapolate(sequence)
    return ans

def solver2(input_file):
    ans = 0
    for line in open(input_file, "r").read().split("\n")[:-1]:
        sequence = [int(i) for i in line.split(" ")]
        ans += baxtrapolate(sequence)
    return ans


def test_part(input, true, part2=False):
    ans = solver1(input) if not part2 else solver2(input)

    if ans != true:
        raise Exception(f"Test part {'2' if part2 else '1'} failed for {input}. Expected {true}, got {ans}")

def unit_tests():
    for line, exp in zip(open("test_input.txt", "r").read().split("\n")[:-1], (18, 28, 68)):
        sequence = [int(i) for i in line.split(" ")]
        ans = extrapolate(sequence)
        assert ans == exp

    for line, exp in zip(open("test_input.txt", "r").read().split("\n")[:-1], (-3, 0, 5)):
        sequence = [int(i) for i in line.split(" ")]
        ans = baxtrapolate(sequence)
        assert ans == exp
        
def main():
    test1 = "test_input.txt" 
    test2 = "test_input.txt" # Update this if two test inputs
    real = "input.txt"

    unit_tests()
    test_part(test1, 114)
    print(f"Part 1: {solver1(real)}")
    test_part(test2, 2, part2=True)
    print(f"Part 2: {solver2(real)}")
    
if __name__ == "__main__":
    main()
