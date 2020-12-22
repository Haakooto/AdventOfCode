p1, p2 = open("input").read().strip().split("\n\n")
deck1 = [int(i) for i in p1.splitlines()[1:]]
deck2 = [int(i) for i in p2.splitlines()[1:]]

while min(len(deck1), len(deck2)):
    if deck1[0] > deck2[0]:
        deck1 += [deck1.pop(0), deck2.pop(0)]
    else:
        deck2 += [deck2.pop(0), deck1.pop(0)]

if deck1 == []:
    winner = deck2
else:
    winner = deck1

score = 0
for idx, val in enumerate(winner[::-1]):
    score += val * (idx + 1)
print(score)


def recursive_combat(d1, d2, level=0):
    seen_1 = []
    seen_2 = []

    while min(len(d1), len(d2)):
        if (h1 := hash(tuple(d1))) in seen_1:
            return True, 420
        else:
            seen_1.append(h1)

        if (h2 := hash(tuple(d2))) in seen_2:
            return True, 69
        else:
            seen_2.append(h2)

        c1 = d1.pop(0)
        c2 = d2.pop(0)
        if c1 <= len(d1) and c2 <= len(d2):
            if recursive_combat([i for i in d1[:c1]], [i for i in d2[:c2]], level+1)[0]:
                d1 += [c1, c2]
            else:
                d2 += [c2, c1]
        else:
            if c1 > c2:
                d1 += [c1, c2]
            else:
                d2 += [c2, c1]

    if d1 == []:
        return False, d2
    else:
        return True, d1


p1, p2 = open("input").read().strip().split("\n\n")
deck1 = [int(i) for i in p1.splitlines()[1:]]
deck2 = [int(i) for i in p2.splitlines()[1:]]

score = 0
for idx, val in enumerate(recursive_combat(deck1, deck2)[1][::-1]):
    score += val * (idx + 1)
print(score)
