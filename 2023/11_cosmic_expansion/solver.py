 import numpy as np

def solver(input_file, expansion_factor=2):
    with open(input_file, "r") as f:
        lines = f.read().split("\n")[:-1]
    space = np.zeros((len(lines), len(lines[0])), dtype=int)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "#":
                space[i, j] = 1

    empty_rows = set(np.where(np.sum(space, axis=1) == 0)[0])
    empty_cols = set(np.where(np.sum(space, axis=0) == 0)[0])
    
    galaxies = np.asarray(np.where(space == 1))
    count = len(galaxies[0])
    dist = 0
    for A in range(count):
        for B in range(A+1, count):
            dist += np.sum(np.abs(galaxies[:, A] - galaxies[:, B]))

            rows = set(np.arange(galaxies[0, A], galaxies[0, B]))
            cols = set(np.arange(galaxies[1, A], galaxies[1, B]))
            if galaxies[1, A] > galaxies[1, B]:
                cols = set(np.arange(galaxies[1, B], galaxies[1, A]))

            row_hits = len(rows.intersection(empty_rows))
            col_hits = len(cols.intersection(empty_cols))
            dist += row_hits * (expansion_factor - 1)
            dist += col_hits * (expansion_factor - 1)
    return dist

def test_part(input, rate, true):
    ans = solver(input, rate)  

    if ans != true:
        raise Exception(f"Test with expansion factor {rate} failed for {input}. Expected {true}, got {ans}")

def main():
    test1 = "test_input.txt" 
    real = "input.txt"

    test_part(test1, 2, 374)
    test_part(test1, 10, 1030)
    test_part(test1, 100, 8410)
    print(f"Part 1: {solver(real)}")    
    print(f"Part 2: {solver(real, 1_000_000)}")

if __name__ == "__main__":
    main()
