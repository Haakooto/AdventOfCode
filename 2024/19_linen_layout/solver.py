def read(file):
    with open(file, "r") as file:
        towels, designs = file.read().split("\n\n")
    return towels.split(", "), designs.split("\n")[:-1]

def count_matches(s, substrings):
    n = len(s)
    dp = [0] * (n + 1)
    dp[n] = 1  # Base case: One way to match an empty string

    for i in range(n - 1, -1, -1):  # Work backwards
        for sub in substrings:
            if s.startswith(sub, i):
                dp[i] += dp[i + len(sub)]
    return dp[0]

def solver_alt2(input_file):
    towels, designs = read(input_file)
    possible = 0
    unique = 0
    for d in designs:
        count = count_matches(d, towels)
        if count:
            possible += 1
        unique += count
    return possible, unique
