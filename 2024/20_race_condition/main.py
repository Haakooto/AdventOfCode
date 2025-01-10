from solver import solver


def main():
    real = "input.txt"

    p1 = solver(real)
    print(f"p1: {p1}")
    p2 = solver(real, part2=True)
    print(f"p2: {p2}")
    
if __name__ == "__main__":
    main()
