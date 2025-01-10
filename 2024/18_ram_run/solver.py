import numpy as np

def read(file):
    with open(file, "r") as file:
        return file.read().split("\n")[:-1]  # Most typical case

def find_path(blocks, sim, size):
    space = np.zeros((size, size))
    for block in blocks[:sim]:
        x, y = block.split(",")
        space[int(y), int(x)] = 1
    space = np.pad(space, 1, constant_values=-1)
    visited = np.zeros_like(space)
    
    around = np.array([[0,-1], [0, 1], [-1, 0], [1, 0]])
    start = np.array([1, 1])[:, None]
    visited[*start] = 1
    queue = [(start, [])]

    while True:
        pos, path = queue.pop(0)
        path.append((tuple(pos[:, 0])))
        
        see = pos.T + around
        valid = (space[*see.T] == 0) & (visited[*see.T] == 0)
        for p in see[valid]:
            visited[*p] = 1
            queue.append((p[:, None], path.copy()))
            if (p == np.array([size, size])).all():
                return path
        if len(queue) == 0:
            return None


def solver_alt2(input_file):
    if "test" in input_file:
        max = 6 + 1
        sim = 12
    else:
        max = 70 + 1
        sim = 1024

    blocks = read(input_file)
    path = find_path(blocks, sim, max)
    shortest = len(path)
    
    for i in range(sim, len(blocks)):
        x, y = blocks[i].split(",")
        if (int(y)+1, int(x)+1) in path:
            path = find_path(blocks, i+1, max)
            if path is None:
                break
            
    return shortest, blocks[i]
