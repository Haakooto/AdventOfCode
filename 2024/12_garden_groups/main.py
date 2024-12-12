alt = 1
verbose = True
from solver import solver_alt1 as solver


def test_part(input, true, part2=False):
    ans = solver(input, part2=part2)  

    if ans != true:
        raise Exception(f"Test part {'2' if part2 else '1'} failed for {input}. Expected {true}, got {ans}")
    if verbose: print(f"Test part {'2' if part2 else '1'} passed for {input}.")

def main():
    part1s = [140, 772, 1930]
    part2s = [80, 436, 1206, 236, 368]
    real = "input.txt"

    for i, sol in enumerate(part1s):
        test = f"test_input_{i+1}.txt", sol
        test_part(*test)
    print(f"Part 1: {solver(real)}")    

    for i, sol in enumerate(part2s):
        test = f"test_input_{i+1}.txt", sol
        test_part(*test, part2=True)

    print(f"Part 2: {solver(real, part2=True)}")
        

if __name__ == "__main__":
    main()
