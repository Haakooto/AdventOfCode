from solver import solver, solver1, solver2


def test_part(input, true, part2=False):
    ans = solver2(input)  
    ans = ans[1] if part2 else ans[0]

    if ans != true:
        raise Exception(f"Test part {'2' if part2 else '1'} failed for {input}. Expected {true}, got {ans}")

def main():
    test1 = "test_input.txt" 
    test2 = "test_input.txt" # Update this if two test inputs
    real = "input.txt"

    test_part(test1, 35)
    p1, p2 = solver2(real)
    print(f"Part 1: {p1}")
    test_part(test2, 46, part2=True)
    print(f"Part 2: {p2}")
    
if __name__ == "__main__":
    main()
