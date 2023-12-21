import numpy as np
from tqdm import tqdm
from bisect import insort
import heapq

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

class Node:
    end = None
    def __init__(self, position, heat, parent=None, direction=up):
        self.position = position
        self.direction = direction
        self.dist = np.abs(self.position - self.end).sum()
        self.directions = set()
        if parent is not None:
            self.parent = parent
            self.integrated_heat = parent.integrated_heat + heat
            if parent.parent is not None:
                if parent.parent.parent is not None:
                    self.directions = set((parent.parent.parent.direction, parent.parent.direction, parent.direction, direction))
        else:   
            self.parent = None
            self.integrated_heat = 0
        self.score = self.integrated_heat + self.dist

    def tiar(self):
        return len(self.directions) == 1
    
    def __eq__(self, other):
        return (self.position == other.position).all()
    
    def __lt__(self, other):
        return self.score < other.score
    
    def __hash__(self) -> int:
        return self.position.tobytes().__hash__()

    def __repr__(self):
        return f"Node({self.position}, {self.integrated_heat}, {self.score})."
    
    def neighbors(self):
        for direction in [up, down, left, right]:
            yield Node(self.position + direction(), 0, None, None)
    
def wander(start, end, city):
    visited = set()
    frontier = [(start.score, start)]
    heapq.heapify(frontier)
    found = False

    i = 0
    while not found:
        i += 1
        _, node = heapq.heappop(frontier)
        visited.add(node)
        if i % 1000 == 0:
            print(f"iter {i}: visited {len(visited)} / {city.size}. Frontier: {len(frontier)}", end='\r')
        for direction in [up, down, left, right]:
            new_pos = node.position + direction()
            if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= city.shape[0] or new_pos[1] >= city.shape[1]:
                continue
            N = Node(new_pos, city[*new_pos], node, direction)
            if N in visited or N.tiar():
                continue
            if (N.position == end).all():
                print(f"iter {i}: visited {len(visited)} / {city.size}. Frontier: {len(frontier)}")
                found = True
                return N
            heapq.heappush(frontier, (N.score, N))
    return

def read_input(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    city = np.array([[int(i) for i in line.strip()] for line in lines], dtype=int)
    return city


def solver_alt1(input_file, part2=False):
    with open(input_file, "r") as file:
        lines = file.read().split("\n")[:-1]  # Most typical case
    # One function that behaves differently depending on part2
    return None

def solver_alt2(input_file):
    with open(input_file, "r") as file:
        lines = file.read().split("\n")[:-1]  # Most typical case
    # One function that returns both part1 and part2
    return None, None

def solver1_alt3(input_file):
    city = read_input(input_file)
    print(city)
    print(city.shape)
    start = np.zeros(2, dtype=int)
    end = np.asarray(city.shape, dtype=int) - 1
    Node.end = end

    final_node = wander(Node(start, city[*start]), end, city)
    visited = np.zeros(city.shape, dtype=int)
    node = final_node
    step = 1
    while node is not None:
        visited[*node.position] = step
        step += 1
        node = node.parent
    print(visited)
    print(final_node.integrated_heat)
    return final_node.integrated_heat # + city[*end]

def solver2_alt3(input_file):
    with open(input_file, "r") as file:
        lines = file.read().split("\n")[:-1]  # Most typical case
    # One function that does part2. Used in conjunction with solver1_alt3
    return None
