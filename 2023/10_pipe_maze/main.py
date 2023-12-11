from solver import *

def test_part(input, true, part2=False):
    ans = solver(input)  
    ans = ans[1] if part2 else ans[0]

    if ans != true:
        raise Exception(f"Test part {'2' if part2 else '1'} failed for {input}. Expected {true}, got {ans}")

def main():
    test1 = "test_input.txt" 
    test2 = "test_input_2.txt"
    test3 = "test_input_3.txt"
    test3b = "test_input_3b.txt"
    test4 = "test_input_4.txt"
    test5 = "test_input_5.txt"
    real = "input.txt"
    
    test_part(test1, 4)
    test_part(test2, 8)
    test_part(test1, 1, part2=True)
    test_part(test2, 1, part2=True)
    test_part(test3, 4, part2=True)
    test_part(test3b, 4, part2=True)
    test_part(test4, 8, part2=True)
    test_part(test5, 10, part2=True)
    
    p1, p2 = solver(real)
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
    
if __name__ == "__main__":
    main()
