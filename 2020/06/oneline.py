cnt = 0
for group in open("i").read().split("\n\n"):
    # form = set()
    # for ans in group.split("\n"):
    # for l in ans:
    form = [len(set(list(form) + list(ans))) for ans in group.split("\n")]
    cnt += sum(form)
print(cnt)

# print(sum([len(set([l for l in ])) for group in open("i").read().split("\n\n")]))
