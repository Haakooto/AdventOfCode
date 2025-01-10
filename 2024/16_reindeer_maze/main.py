alt = 2
verbose = True

if alt == 1:
    from solver import solver_alt1 as solver
elif alt == 2:
    from solver import solver_alt2 as solver
elif alt == 3:
    from solver import solver1_alt3 as solver1, solver2_alt3 as solver2


def test_part(input, true1, true2):
    ans1, ans2 = solver(input)  

    if ans1 != true1:
        raise Exception(f"Test part 1 failed for {input}. Expected {true1}, got {ans1}")
    if ans2 != true2:
        raise Exception(f"Test part 2 failed for {input}. Expected {true2}, got {ans2}")
    if verbose: print(f"Test passed for {input}.")
    
def unit_tests(input_file, expected, part2=False):
    if expected == (None, None):
        return
    from solver import func_that_does_the_thing
    for i, (input, exp) in enumerate(zip(open(input_file, "r").read().split("\n")[:-1], expected)):
        ans = func_that_does_the_thing(input, part2=part2)

        if ans != exp:
            raise Exception(f"Unit test {i+1} failed. Expected {exp}, got {ans}")
    if verbose: print(f"Unit tests passed for part {'2' if part2 else '1'}!")
        

def main():
    test1 = "test_input.txt", 7036, 45
    test2 = "test_input_2.txt", 11048, 64
    real = "input.txt"

    if alt == 1:
        test_part(*test1)
        test_part(*test2)
        print(f"Part 1: {solver(real)}")    
        test_part(*test2, part2=True)
        print(f"Part 2: {solver(real, part2=True)}")
        
    elif alt == 2:
        test_part(*test1)
        test_part(*test2)
        p1, p2 = solver(real)
        print(f"Part 1: {p1}")
        print(f"Part 2: {p2}")
        
    elif alt == 3:
        test_part(*test1)
        print(f"Part 1: {solver1(real)}")
        test_part(*test2, part2=True)
        print(f"Part 2: {solver2(real)}")
    
if __name__ == "__main__":
    main()
