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


def solver_alt1(input_file, part2=False):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    grid = np.array([[i for i in line.strip()] for line in lines], dtype=str)
    energized = np.zeros_like(grid, dtype=int)

    position = np.array([0, -1])

    ray_splits = [Ray(position, right)]
    while len(ray_splits) > 0:
        ray = ray_splits.pop(0)
        print(f"New ray, starting at {ray.position}, going {ray.direction.__name__}")
        while ray.alive:
            print(energized)
            print(ray.position, ray.direction.__name__, ray.direction())
            print()
            ray.move()
            if ray.position[0] < 0 or ray.position[1] < 0 or ray.position[0] >= grid.shape[0] or ray.position[1] >= grid.shape[1]:
                ray.alive = False
                print("Hit wall, died")
                continue
            if energized[*ray.position] in (3, 4):
                ray.alive = False
                print("Deja vu")
                continue

            if grid[*ray.position] == ".":
                energized[*ray.position] += 1 if ray.direction in (up, down) else 2
            elif grid[*ray.position] == "\\":
                if ray.direction == left:
                    ray.turn(up)
                    energized[*ray.position] += 1
                elif ray.direction == up:
                    ray.turn(left)
                    energized[*ray.position] += 2
                elif ray.direction == right:
                    ray.turn(down)
                    energized[*ray.position] += 2
                elif ray.direction == down:
                    ray.turn(right)
                    energized[*ray.position] += 1
            elif grid[*ray.position] == "/":
                if ray.direction == left:
                    ray.turn(down)
                    energized[*ray.position] += 1
                elif ray.direction == up:
                    ray.turn(right)
                    energized[*ray.position] += 1
                elif ray.direction == right:
                    ray.turn(up)
                    energized[*ray.position] += 2
                elif ray.direction == down:
                    ray.turn(left)
                    energized[*ray.position] += 2
            elif grid[*ray.position] == "|":
                if ray.direction in (left, right):
                    ray_splits.append(Ray(ray.position.copy(), up))
                    ray.turn(down)
                    energized[*ray.position] += 1
                else:
                    energized[*ray.position] += 2
            elif grid[*ray.position] == "-":
                if ray.direction in (up, down):
                    ray_splits.append(Ray(ray.position.copy(), left))
                    ray.turn(right)
                    energized[*ray.position] += 1
                else:
                    energized[*ray.position] += 2
            input()

    print(energized)
    # One function that behaves differently depending on part2
    return None

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
