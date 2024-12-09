
def read(file):
    with open(file, "r") as file:
        d = file.read().split("\n")[0]
    return [int(i) for i in d]

def alt_solver_slow(input_file):
    # Much slower, but works
    disk = read(input_file)
    odisk = []
    id = 0
    for i, d in enumerate(disk):
        if i % 2 == 0:
            odisk += [id,] * d
            id += 1
        else:
            odisk += [None,] * d
    while None in odisk:
        new = odisk.index(None)
        old = odisk.pop(-1)
        odisk[new] = old
        while odisk[-1] is None:
            odisk = odisk[:-1]
    checksum = sum([i * v for i, v in enumerate(odisk)])
    return checksum

def solver1_alt3(input_file):
    disk = read(input_file)
    files = []
    free = []

    head = 0
    for i, d in enumerate(disk):
        if i % 2 == 0:
            id = i // 2
            for _ in range(disk[i]):
                files.append([head, id])
                head += 1
        else:
            for _ in range(disk[i]):
                free.append(head)
                head += 1
                
    for file in files[::-1]:
        space = free.pop(0)
        if file[0] >= space:
            file[0] = space  # move file
        if len(free) == 0:
            break

    checksum = 0
    for file in files:
        start, id = file
        checksum += id * start
    return checksum

def solver2_alt3(input_file):
    disk = read(input_file)
    files = []
    free = []

    head = 0
    for i, d in enumerate(disk):
        if i % 2 == 0:
            id = i // 2
            files.append([head, disk[i], id])
        else:
            free.append([head, disk[i]])
        head += disk[i]
    
    for file in files[::-1]:
        # file = [start, length, id]
        for space in free:
            if file[0] < space[0]:
                continue
            # space = [start, length]
            if space[1] >= file[1]:
                file[0] = space[0]  # move file
                space[1] -= file[1]  # reduce space length
                space[0] += file[1]
                break
        # filter out taken spaces
        free = [space for space in free if space[1] != 0]

    checksum = 0
    for file in files:
        start, length, id = file
        agg = length * start + (length - 1) * (length) // 2
        checksum += id * agg
    return checksum
