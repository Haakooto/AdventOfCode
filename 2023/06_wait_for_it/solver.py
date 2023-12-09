import re
from tqdm import tqdm

def solver1(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    times = [int(n) for n in re.findall(r'\d+', lines[0].split(":")[1])]
    distances = [int(n) for n in re.findall(r'\d+', lines[1].split(":")[1])]
    accumulated = 1
    for time, dist in zip(times, distances):
        wins = 0
        for i in range(1, time // 2 + 1):
            # print(i, time - i, i * (time - i))
            if i * (time - i) > dist:
                wins += 2
        if time % 2 == 0:
            wins -= 1
        accumulated *= wins
    return accumulated

def solver2(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    time = int("".join(re.findall(r'\d+', lines[0].split(":")[1])))
    distance = int("".join(re.findall(r'\d+', lines[1].split(":")[1])))
    wins = 0
    for i in tqdm(range(1, time // 2 + 1)):
        if i * (time - i) > distance:
            wins += 2
    if time % 2 == 0:
        wins -= 1
    return wins


def test_part(input, true, part2=False):
    ans = solver1(input) if not part2 else solver2(input)

    if ans != true:
        raise Exception(f"Test part {'2' if part2 else '1'} failed for {input}. Expected {true}, got {ans}")

def main():
    test1 = "test_input.txt" 
    test2 = "test_input.txt" # Update this if two test inputs
    real = "input.txt"

    test_part(test1, 288)
    print(f"Part 1: {solver1(real)}")
    test_part(test2, 71503, part2=True)
    print(f"Part 2: {solver2(real)}")
    
if __name__ == "__main__":
    main()
