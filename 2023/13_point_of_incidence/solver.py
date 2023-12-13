import numpy as np

def reflect(pattern, part2):
    rows = pattern.shape[0]
    for r in range(1, rows):
        width = rows - r if r > rows/2 else r
        start = max(0, r - width)
        end = min(rows, r + width)
        upper = pattern[start:r]
        lower = pattern[r:end]
        if np.sum(upper != lower[::-1]) == part2:
            return r
    return 0

def get_reflection_line(pattern, part2=False):
    pattern = pattern.replace(".", "0").replace("#", "1")
    pattern = np.array([list(line) for line in pattern.strip().split("\n")], dtype=int)
    if (cols:=reflect(pattern.T, part2)):
        return cols
    else:
        return reflect(pattern, part2) * 100

def solver(input_file, part2=False):
    sum = 0
    with open(input_file, "r") as f:
        pattern = f.read().strip().split("\n\n")
    for p in pattern:
        sum += get_reflection_line(p, part2=int(part2))
    return sum


def test_part(input, true, part2=False):
    ans = solver(input, part2=part2)  

    if ans != true:
        raise Exception(f"Test part {'2' if part2 else '1'} failed for {input}. Expected {true}, got {ans}")
    
def unit_tests():
    for i, (pattern, exp) in enumerate(zip(open("test_input.txt", "r").read().split("\n\n"), (5, 400))):
        ans = get_reflection_line(pattern)

        if ans != exp:
            raise Exception(f"Unit test {i+1} failed. Expected {exp}, got {ans}")
    for i, (pattern, exp) in enumerate(zip(open("test_input.txt", "r").read().split("\n\n"), (300, 100))):
        ans = get_reflection_line(pattern, part2=True)

        if ans != exp:
            raise Exception(f"Unit test {i+1} failed. Expected {exp}, got {ans}")
        
    print("All unit tests passed")

def main():
    test1 = "test_input.txt", 405
    test2 = "test_input.txt", 400
    real = "input.txt"

    unit_tests()
    test_part(*test1)
    print(f"Part 1: {solver(real)}")    
    test_part(*test2, part2=True)
    print(f"Part 2: {solver(real, part2=True)}")

if __name__ == "__main__":
    main()
