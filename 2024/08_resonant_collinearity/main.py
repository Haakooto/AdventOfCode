alt = 1
verbose = True

if alt == 1:
    from solver import solver_alt1 as solver
elif alt == 2:
    from solver import solver_alt2 as solver
elif alt == 3:
    from solver import solver1_alt3 as solver1, solver2_alt3 as solver2


def test_part(input, true, part2=False):
    if alt == 1:
        ans = solver(input, part2=part2)  

    elif alt == 2:
        ans = solver(input)  
        ans = ans[1] if part2 else ans[0]

    elif alt == 3:
        ans = solver1(input) if not part2 else solver2(input)

    if ans != true:
        raise Exception(f"Test part {'2' if part2 else '1'} failed for {input}. Expected {true}, got {ans}")
    if verbose: print(f"Test part {'2' if part2 else '1'} passed for {input}.")
    

def main():
    test1 = "test_input.txt", 14 
    test2 = "test_input.txt", 34
    real = "input.txt"

    if alt == 1:
        test_part(*test1)
        print(f"Part 1: {solver(real)}")    
        test_part(*test2, part2=True)
        print(f"Part 2: {solver(real, part2=True)}")
        
    elif alt == 2:
        test_part(*test1)
        p1, p2 = solver(real)
        print(f"Part 1: {p1}")
        test_part(*test2, part2=True)
        print(f"Part 2: {p2}")
        
    elif alt == 3:
        test_part(*test1)
        print(f"Part 1: {solver1(real)}")
        test_part(*test2, part2=True)
        print(f"Part 2: {solver2(real)}")
    
if __name__ == "__main__":
    main()
