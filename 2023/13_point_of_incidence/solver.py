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
    
def unit_tests(input_file, expected, part2=False):
    for i, (input, exp) in enumerate(zip(open(input_file, "r").read().split("\n\n"), expected)):
        ans = get_reflection_line(input, part2=part2)
        if ans != exp:
            raise Exception(f"Unit test {i+1} failed. Expected {exp}, got {ans}")
        

def main():
    test1 = "test_input.txt", 405
    test2 = "test_input.txt", 400
    real = "input.txt"

    unit_tests(test1[0], (5, 400), part2=False)
    unit_tests(test2[0], (300, 100), part2=True)

    test_part(*test1)
    print(f"Part 1: {solver(real)}")    
    test_part(*test2, part2=True)
    print(f"Part 2: {solver(real, part2=True)}")

if __name__ == "__main__":
    main()
