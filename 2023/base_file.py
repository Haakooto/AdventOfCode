# alt 1
def solver(input_file, part2=False):
    return 1

# alt 2
def solver(input_file):
    return 1, 2

# alt 3
def solver1(input_file):
    return 1

def solver2(input_file):
    return 2


def test_part(input, true, part2=False):
    # alt 1
    ans = solver(input, part2=part2)  

    # alt 2
    ans = solver(input)  
    ans = ans[1] if part2 else ans[0]

    # alt 3
    ans = solver1(input) if not part2 else solver2(input)

    if ans != true:
        raise Exception(f"Test part {'2' if part2 else '1'} failed for {input}. Expected {true}, got {ans}")

def main():
    test1 = "test_input.txt" 
    test2 = "test_input.txt" # Update this if two test inputs
    real = "input.txt"

    # alt 1
    test_part(test1, None)
    print(f"Part 1: {solver(real)}")    
    test_part(test2, None, part2=True)
    print(f"Part 2: {solver(real, part2=True)}")
    
    # alt 2
    test_part(test1, None)
    p1, p2 = solver(real)
    print(f"Part 1: {p1}")
    test_part(test2, None, part2=True)
    print(f"Part 2: {p2}")
    
    # alt 3
    test_part(test1, None)
    print(f"Part 1: {solver1(real)}")
    test_part(test2, None, part2=True)
    print(f"Part 2: {solver2(real, part2=True)}")
    
if __name__ == "__main__":
    main()
