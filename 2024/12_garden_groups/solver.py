import re

import numpy as np

class Unit:
    def __init__(self, typ, loc=None):
        self.val = typ
        self.id = None
        self.in_region = None
        self.perims = np.zeros(4)
        if loc:
            self.x, self.y = loc
            self.id = Unit.id
            Unit.id += 1
            Unit.all[self.id] = self
            
    def __repr__(self):
        if self.id is None:
            return f"{self.val}(x,y)"
        return f"{self.val}({self.x},{self.y})"

    def __eq__(self, other):
        return self.id == other.id

    def __or__(self, other):
        return self.val == other.val

    @classmethod
    def reset(cls):
        Unit.id = 1
        Unit.all = {}

class Region:
    mp = {0: 1, 1: 0, 2:3, 3:2}
    def __init__(self, initial, farm):
        if initial.in_region is None:
            self.id = Region.id
            Region.id += 1

            initial.in_region = self.id
            self.units = [initial]
            self.expand(self.units, farm)
            Region.all.append(self)

    def expand(self, frontier, farm):
        new = []
        for unit in frontier:
            for i, (dx, dy) in enumerate(((-1, 0), (1, 0), (0, -1), (0, 1))):
                u = farm[unit.x+dx, unit.y+dy]
                if unit | u:
                    unit.perims[i] = u.id
                    u.perims[Region.mp[i]] = unit.id
                    if u.in_region is None:
                        u.in_region = self.id
                        new.append(u)
        self.units += new
        if len(new) != 0:
            self.expand(new, farm)

    def __repr__(self):
        return f"{self.id}: {self.units}"

    @property
    def area(self):
        return len(self.units)

    @property
    def perimeter(self):
        return sum([sum(u.perims == 0) for u in self.units])

    @classmethod
    def reset(cls):
        Region.id = 0
        Region.all = []

def get_perimeter(reg, part2=False):
    p = reg.perimeter
    if not part2:
        return p

    for u in reg.units:
        for q in u.perims:
            if q != 0:
                q = Unit.all[q]
                eq = u.perims == q.perims
                p -= sum(eq) / 2
    return p


def solver_alt1(file_name, part2=False):
    Unit.reset()
    Region.reset()
    with open(file_name, "r") as f:
        farm = f.read().strip().split("\n")
    farm = np.asarray([[Unit(v, (r+1, c+1)) for c, v in enumerate(row)] for r, row in enumerate(farm)])
    farm = np.pad(farm, 1, constant_values=Unit("#"))
    
    for u in farm[1:-1, 1:-1].flatten():
        Region(u, farm)
    
    price = 0
    for r in Region.all:
        p = get_perimeter(r, part2=part2)
        price += r.area * p
    return int(price)
