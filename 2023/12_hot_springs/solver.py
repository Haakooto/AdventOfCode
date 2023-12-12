import re
from copy import deepcopy

# # alt 1
# def solver(input_file, part2=False):
#     return 1

# # alt 2
# def solver(input_file):
#     return 1, 2

def parse(line):
    springs, groups = line.split(" ")
    groups = [int(i) for i in groups.split(",")]
    return springs, groups

def arrangements(springgroup):
    springs, groups = springgroup
    springs = re.sub(r'(?:^\.+)|(?:\.+$)|(\.)\1+', r'\1', springs)

    g = list(re.finditer(r'\#+', springs))
    # Some simplifications, drop trivial groups from the ends
    while len(g) > 0:
        this = g[0]
        length = this.end() - this.start()
        if length == groups[0]:
            groups.pop(0)
            g.pop(0)
            springs = springs[this.end()+1:]
        else:
            break

    while len(g) > 0:
        length = g[-1].end() - g[-1].start()
        if length == groups[-1]:
            springs = springs[:g[-1].start()-1]
            groups.pop(-1)
            g.pop(-1)
        else:
            break

    if sum(groups) + len(groups) - 1 == len(springs):  
        print("Here")
        return 1  # contstrained to only allow 1 solution
    if len(groups) == 1:
        print(groups, springs)
        print("Using this")
        return len(springs)
    
    return None

    print(f"{groups=}")
    print(f"{springs=}")
    print(f"{sum(groups) + len(groups) - 1}")
    print(f"{len(springs)}") 
    return 0 

# alt 3
def solver1(input_file):
    with open(input_file, "r") as f:
        lines = f.read().split("\n")[:-1]
    
    sum = 0
    for line in lines:
        sequence = parse(line)
        sum += arrangements(sequence)
    return sum

def solver2(input_file):
    return 2


def test_part(input, true, part2=False):
    # # alt 1
    # ans = solver(input, part2=part2)  

    # # alt 2
    # ans = solver(input)  
    # ans = ans[1] if part2 else ans[0]

    # alt 3
    ans = solver1(input) if not part2 else solver2(input)

    if ans != true:
        raise Exception(f"Test part {'2' if part2 else '1'} failed for {input}. Expected {true}, got {ans}")
    
def unit_tests():
    for i, (line, exp) in enumerate(zip(open("test_input.txt", "r").read().split("\n")[:-1], (1, 4, 1, 1, 4, 10))):
        ans = arrangements(parse(line))
        if ans is None:
            continue

        if ans != exp:
            raise Exception(f"Unit test {i} failed. Expected {exp}, got {ans}")

    for i, (line, exp) in enumerate(zip(open("test_input_2.txt", "r").read().split("\n")[:-1], (12, 1, 16, 6, 7, 3, 6, 4, 1, 2))):
        ans = arrangements(parse(line))
        if ans is None:
            continue

        if ans != exp:
            raise Exception(f"Unit test {i} failed. Expected {exp}, got {ans}")

def main():
    test1 = "test_input.txt" 
    test2 = "test_input.txt" # Update this if two test inputs
    real = "input.txt"

    # # alt 1
    # test_part(test1, 21)
    # print(f"Part 1: {solver(real)}")    
    # test_part(test2, None, part2=True)
    # print(f"Part 2: {solver(real, part2=True)}")
    
    # # alt 2
    # test_part(test1, None)
    # p1, p2 = solver(real)
    # print(f"Part 1: {p1}")
    # test_part(test2, None, part2=True)
    # print(f"Part 2: {p2}")
    
    # alt 3
    unit_tests()
    # test_part(test1, 21)
    # print(f"Part 1: {solver1(real)}")
    # test_part(test2, None, part2=True)
    # print(f"Part 2: {solver2(real, part2=True)}")
    
if __name__ == "__main__":
    main()
