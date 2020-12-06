count_1 = 0
form_1 = []

count_2 = 0
form_2 = []

for line in open("i").read().split("\n"):
    if line == "":
        count_1 += len(set(form_1))
        form_1 = []

        leader = set(form_2[0])
        for memb in form_2[1:]:
            leader.intersection_update(memb)
        count_2 += len(leader)
        form_2 = []
    else:
        form_2.append([j for j in line.strip()])
        for i in line.strip():
            form_1.append(i)

print(count_1)
print(count_2)

