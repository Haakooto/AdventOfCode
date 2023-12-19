alt = 1

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
        raise Exception(
            f"Test part {'2' if part2 else '1'} failed for {input}. Expected {true}, got {ans}"
        )


def unit_tests(input_file, expected_file, part2=False):
    from solver import north, parse_input

    board = parse_input(input_file)
    tilted_board = north(board)
    true_board = parse_input(expected_file)
    
    errors = sum((true_board != tilted_board).flatten())
    if errors != 0:
        raise Exception(f"Unit test failed. There was {errors} errors.")
    print("Unit test passed.")

def cycle_tests(input_file, expected_file, part2=False):
    from solver import cycle, parse_input

    board = parse_input(input_file)
    true_board = parse_input(expected_file)
    for _ in range(part2):
        board = cycle(board)

    errors = sum((true_board != board).flatten())
    if errors != 0:
        raise Exception(f"Unit test failed. There was {errors} errors.")
    print("Cycling test passed.")


def main():
    test1 = "test_input.txt", 136
    test2 = "test_input.txt", 64
    real = "input.txt"

    unit_tests(test1[0], "test_output.txt", part2=False)
    cycle_tests(test1[0], "cycle_1.txt", part2=1)
    cycle_tests(test1[0], "cycle_2.txt", part2=2)
    cycle_tests(test1[0], "cycle_3.txt", part2=3)

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
