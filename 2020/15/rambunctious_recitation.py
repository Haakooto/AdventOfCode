input = "14,8,16,0,1,17"
# N = 2020
N = 30000000
spoken = {}
for i, n in enumerate(input.split(",")):
    prev = int(n)
    spoken[int(n)] = i + 1

turn = i
while True:
    turn += 1
    if prev in spoken:
        since = turn - spoken[prev]
    else:
        since = 0
    spoken[prev] = turn
    if turn == N:
        break
    prev = since

print(prev)

