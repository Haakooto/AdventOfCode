from solver import solver

def test_part(input, true, part2=False):
    ans = solver(input, part2=part2)

    if ans != true:
        raise Exception(f"Test part {'2' if part2 else '1'} failed for {input}. Expected {true}, got {ans}")

def main():
    test1 = "test_input.txt" 
    test2 = "test_input.txt" # Update this if two test inputs
    real = "input.txt"

    # alt 1
    test_part(test1, 6440)
    print(f"Part 1: {solver(real)}")    
    test_part(test2, 5905, part2=True)
    print(f"Part 2: {solver(real, part2=True)}")
    
if __name__ == "__main__":
    main()
