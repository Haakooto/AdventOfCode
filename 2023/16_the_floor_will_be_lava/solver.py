import numpy as np

def func_that_does_the_thing(input, part2=False):
    # Do the thing. For when the input is a list of inputs treated separately
    return None

def up():
    return np.array([-1, 0])
def down():
    return np.array([1, 0])
def left():
    return np.array([0, -1])
def right():
    return np.array([0, 1])

class Ray:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        self.alive = True

    def move(self):
        self.position += self.direction()

    def turn(self, new_direction):
        self.direction = new_direction

def scatter_rays(grid, ray_splits):
    energized = np.zeros((*grid.shape, 2), dtype=int)
    while len(ray_splits) > 0:
        ray = ray_splits.pop(0)
        while ray.alive:
            ray.move()
            if ray.position[0] < 0 or ray.position[1] < 0 or ray.position[0] >= grid.shape[0] or ray.position[1] >= grid.shape[1]:
                ray.alive = False
                continue

            if grid[*ray.position] == ".":
                energized[*ray.position][0 if ray.direction in (up, down) else 0] = 1
            elif grid[*ray.position] == "\\":
                if ray.direction == left:
                    if energized[*ray.position][0] == 1:
                        ray.alive = False
                        continue
                    ray.turn(up)
                    energized[*ray.position][0] = 1
                elif ray.direction == up:
                    if energized[*ray.position][1] == 1:
                        ray.alive = False
                        continue
                    ray.turn(left)
                    energized[*ray.position][1] = 1
                elif ray.direction == right:
                    if energized[*ray.position][1] == 1:
                        ray.alive = False
                        continue
                    ray.turn(down)
                    energized[*ray.position][1] = 1
                elif ray.direction == down:
                    if energized[*ray.position][0] == 1:
                        ray.alive = False
                        continue
                    ray.turn(right)
                    energized[*ray.position][0] = 1
            elif grid[*ray.position] == "/":
                if ray.direction == left:
                    if energized[*ray.position][0] == 1:
                        ray.alive = False
                        continue
                    ray.turn(down)
                    energized[*ray.position][0] = 1
                elif ray.direction == up:
                    if energized[*ray.position][0] == 1:
                        ray.alive = False
                        continue
                    ray.turn(right)
                    energized[*ray.position][0] = 1
                elif ray.direction == right:
                    if energized[*ray.position][1] == 1:
                        ray.alive = False
                        continue
                    ray.turn(up)
                    energized[*ray.position][1] = 1
                elif ray.direction == down:
                    if energized[*ray.position][1] == 1:
                        ray.alive = False
                        continue
                    ray.turn(left)
                    energized[*ray.position][1] = 1
            elif grid[*ray.position] == "|":
                if ray.direction in (left, right):
                    if energized[*ray.position][0] == 1:
                        ray.alive = False
                        continue
                    ray_splits.append(Ray(ray.position.copy(), up))
                    ray.turn(down)
                    energized[*ray.position][0] = 1
                else:
                    if energized[*ray.position][1] == 1:
                        ray.alive = False
                        continue
                    energized[*ray.position][1] = 1
            elif grid[*ray.position] == "-":
                if ray.direction in (up, down):
                    if energized[*ray.position][0] == 1:
                        ray.alive = False
                        continue
                    ray_splits.append(Ray(ray.position.copy(), left))
                    ray.turn(right)
                    energized[*ray.position][0] = 1
                else:
                    if energized[*ray.position][1] == 1:
                        ray.alive = False
                        continue
                    energized[*ray.position][1] = 1
    return np.sum(np.logical_or(energized[..., 0], energized[..., 1]))

def solver_alt1(input_file, part2=False):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    grid = np.array([[i for i in line.strip()] for line in lines], dtype=str)
    
    if not part2:
        position = np.array([0, -1])
        ray_splits = [Ray(position, right)]
        return scatter_rays(grid, ray_splits)

    max_energy = 0
    for i in range(grid.shape[0]):
        position = np.array([i, -1])
        ray_splits = [Ray(position, right)]
        max_energy = max(max_energy, scatter_rays(grid, ray_splits))
    for i in range(grid.shape[1]):
        position = np.array([-1, i])
        ray_splits = [Ray(position, down)]
        max_energy = max(max_energy, scatter_rays(grid, ray_splits))
    for i in range(grid.shape[0]):
        position = np.array([i, grid.shape[1]])
        ray_splits = [Ray(position, left)]
        max_energy = max(max_energy, scatter_rays(grid, ray_splits))
    for i in range(grid.shape[1]):
        position = np.array([grid.shape[0], i])
        ray_splits = [Ray(position, up)]
        max_energy = max(max_energy, scatter_rays(grid, ray_splits))
    return max_energy

def solver_alt2(input_file):
    with open(input_file, "r") as file:
        lines = file.read().split("\n")[:-1]  # Most typical case
    # One function that returns both part1 and part2
    return None, None

def solver1_alt3(input_file):
    with open(input_file, "r") as file:
        lines = file.read().split("\n")[:-1]  # Most typical case
    # One function that does part1. Used in conjunction with solver2_alt3
    return None

def solver2_alt3(input_file):
    with open(input_file, "r") as file:
        lines = file.read().split("\n")[:-1]  # Most typical case
    # One function that does part2. Used in conjunction with solver1_alt3
    return None
