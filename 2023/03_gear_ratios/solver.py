import numpy as np
import re

def solver1(input_file):
    engine = np.loadtxt(input_file, dtype=str, comments=None)
    parts = 0
    for i, line in enumerate(engine):
        for m in re.finditer(r'\d+', line):
            start, end = m.span()
            number = m.group()
            for j in range(i-1, i+2):
                if j < 0 or j >= len(engine):
                    continue
                search = engine[j][max(start-1, 0):end+1]
                search = search.replace(".", "").replace(number, "")
                if len(search) != 0:
                    parts += int(number)
                    break
    return parts

def solver2(input_file):
    engine = np.loadtxt(input_file, dtype=str, comments=None)
    ratios = 0
    for i, line in enumerate(engine):
        for gear in re.finditer(r'\*', line):
            gear = gear.start()
            ratio = []
            for j in range(i-1, i+2):
                if j < 0 or j >= len(engine):
                    continue
                for nums in re.finditer(r'\d+', engine[j]):
                    s, e = nums.span()
                    if s-1 <= gear and e >= gear:
                        ratio.append(int(nums.group()))
            if len(ratio) == 2:
                ratios += ratio[0] * ratio[1]
    return ratios

def test_part(input, true, part2=False):
    ans = solver1(input) if not part2 else solver2(input)
    if ans != true:
        raise Exception(f"Test part 1 failed for {input}. Expected {true}, got {ans}")

def main():
    test1 = "test_input.txt" 
    real = "input.txt"

    test_part(test1, 4361)
    print(f"Part 1: {solver1(real)}")
    
    test_part(test1, 467835, part2=True)
    print(f"Part 2: {solver2(real)}")
    
if __name__ == "__main__":
    main()
