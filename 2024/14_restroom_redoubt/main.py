alt = 2
verbose = True

if alt == 1:
    from solver import solver_alt1 as solver
elif alt == 2:
    from solver import solver_alt2 as solver
elif alt == 3:
    from solver import solver1_alt3 as solver1, solver2_alt3 as solver2

def main():
    real = "input.txt"

    p1, p2 = solver(real)
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
    
if __name__ == "__main__":
    main()
