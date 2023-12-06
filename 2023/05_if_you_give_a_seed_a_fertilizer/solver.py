from collections import defaultdict
import numpy as np
from tqdm import tqdm

class Lambda:
    def __init__(self, source=None, dest=None, range=None):
        self.source = source
        self.dest = dest
        self.range = range

    def __call__(self, x):
        return x - (self.source - self.dest)
    
class Mapper:
    def __init__(self, dest_name, funcs):
        self.dest_name = dest_name
        self.funcs = np.array(funcs, dtype=object)
        self.mins = np.array([func.source for func in funcs])
        self.maxs = np.array([func.source + func.range for func in funcs])

    def __call__(self, x):
        i = list(np.where(np.logical_and(self.mins <= x, x < self.maxs))[0])
        if i:
            new = self.funcs[i[0]](x)
            return new, self.dest_name
        return x, self.dest_name
            

# alt 1
def solver(input_file, part2=False):
    return 1

# alt 2
def solver(input_file):
    with open(input_file, 'r') as f:
        sections = f.read().split("\n\n")
    seeds = [int(seed) for seed in sections[0].split(" ")[1:]]
    converters = defaultdict(defaultdict)
    for section in sections[1:]:
        lines = section.split("\n")
        source, _, destination = lines[0].split(" ")[0].split("-")
        converters[source]["to"] = destination
        converters[source]["funcs"] = []
        for line in lines[1:]:
            if line == "":
                continue
            dest_from, source_from, range_val = [int(x) for x in line.split(" ")]
            converters[source]["funcs"].append(Lambda(source_from, dest_from, range_val))
        converters[source]["funcs"].append(lambda x: x)

        
    def seed_to_location(original_seed, cache={}):
        if original_seed in cache:
            return cache[original_seed], cache
        seed = original_seed
        source = "seed"
        while source != "location":
            for func in converters[source]["funcs"]:
                new = func(seed)
                if new is not None:
                    seed = new
                    break
            source = converters[source]["to"]
        cache[original_seed] = seed
        return seed, cache

    part1 = 1e9
    cache = {}
    for oseed in seeds:
        seed, cache = seed_to_location(oseed, cache)
        if seed < part1:
            part1 = seed

    part2 = 1e9
    # for i in range(0, len(seeds), 2):
    #     for seed in range(seeds[i], seeds[i] + seeds[i+1]):
    #         seed, cache = seed_to_location(seed, cache)
    #         if seed < part2:
    #             part2 = seed

    return part1, part2

# alt 3
def solver1(input_file):
    return 1

def solver2(input_file):
    with open(input_file, 'r') as f:
        sections = f.read().split("\n\n")
    seeds = [int(seed) for seed in sections[0].split(" ")[1:]]
    forward_converters = {}
    backward_converters = {}
    for section in sections[1:]:
        lines = section.split("\n")
        source, _, destination = lines[0].split(" ")[0].split("-")
        forward_funcs = []
        backward_funcs = []
        for line in lines[1:]:
            if line == "":
                continue
            dest_from, source_from, range_val = [int(x) for x in line.split(" ")]
            forward_funcs.append(Lambda(source_from, dest_from, range_val))
            backward_funcs.append(Lambda(dest_from, source_from, range_val))
        forward_converters[source] = Mapper(destination, forward_funcs)
        backward_converters[destination] = Mapper(source, backward_funcs)

    print(backward_converters["location"].mins)
    print(backward_converters["location"].maxs)
    return
        
    part1 = 1e9
    for seed in seeds:
        source = "seed"
        for _ in range(7):
            seed, source = forward_converters[source](seed)
        if seed < part1:
            part1 = seed
    print(part1)

    known_max = 278755257
    # known_max = 27875525
    known_min = 2787552
    known_min = 24000000
    known_min = 26259221
    known_exe = 26829166


    location = -1
    part2 = None
    with tqdm(total=known_max) as pbar:
        while part2 is None:
            pbar.update(1)
            location += 1
            source = "location"
            seed = location
            for _ in range(7):
                seed, source = backward_converters[source](seed)
            for i in range(0, len(seeds), 2):
                if seeds[i] <= seed < seeds[i] + seeds[i+1]:
                    part2 = location
                    break

    print(part2)

    return part1, part2

