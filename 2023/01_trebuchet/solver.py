import re

def solver(input_file, part2=False):
    letters = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    numbers = {v: v for k, v in letters.items()}
    converter = numbers
    if part2:
        converter = {**numbers, **letters}
        
    sum = 0
    for line in open(input_file, 'r').read().split("\n")[:-1]:
        matches = "|".join(converter.keys())
        pattern = fr'(?=({matches}))'
        nums = re.findall(pattern, line)
        sum += int(converter[nums[0]] + converter[nums[len(nums)-1]])
    return sum

def test_part1(input, true):
    ans = solver(input)
    if ans != true:
        raise Exception(f"Test part 1 failed for {input}. Expected {true}, got {solver(input)}")

def test_part2(input, true):
    ans = solver(input, part2=True)
    if ans != true:
        raise Exception(f"Test part 2 failed for {input}. Expected {true}, got {solver(input, part2=True)}")

def main():
    test1 = "test_input.txt" 
    test2 = "test_input_2.txt" 
    real = "input.txt"

    test_part1(test1, 142)
    print(f"Part 1: {solver(real)}")

    test_part2(test2, 281)
    print(f"Part 2: {solver(real, part2=True)}")
    
if __name__ == "__main__":
    main()
