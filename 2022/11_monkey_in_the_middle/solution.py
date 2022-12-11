import numpy as np


class Monkey:
    gang = []
    count = 36
    lcd = 1

    def __init__(self, info, worry_manager):
        lines = info.split("\n")
        self.id = int(lines[0].split(" ")[-1][:-1])
        self.items = np.zeros(Monkey.count)
        self.count = 0

        self.operation = eval(f"lambda old: {lines[2].split('=')[-1]}")
        self.divisor = int(lines[3].split(" ")[-1])
        self.true = int(lines[4].split(" ")[-1])
        self.false = int(lines[5].split(" ")[-1])
        self.wm = worry_manager
        self.inspections = 0

        for i in lines[1].split(": ")[1].split(","):
            self.throw(int(i))

        Monkey.gang.append(self)
        Monkey.lcd *= self.divisor

    def throw(self, val):
        self.items[self.count] = val
        self.count += 1

    def __str__(self):
        return f"Monkey {self.id}: {self.items}"

    def turn(self):
        self.inspections += self.count
        self.items = self.operation(self.items) // self.wm
        divisible = self.items % self.divisor

        for i in range(self.count):
            if divisible[i]:
                Monkey.gang[self.false].throw(self.items[i] % Monkey.lcd)
            else:
                Monkey.gang[self.true].throw(self.items[i] % Monkey.lcd)

        self.count = 0
        self.items *= 0

    @staticmethod
    def Reset():
        Monkey.gang = []
        Monkey.lcd = 1


def part1():
    for monkey in open("input").read().strip().split("\n\n"):
        Monkey(monkey, 3)

    for r in range(20):
        for monkey in Monkey.gang:
            monkey.turn()

    actives = sorted([monkey.inspections for monkey in Monkey.gang])
    business = actives[-1] * actives[-2]
    print(business)


def part2():
    for monkey in open("input").read().strip().split("\n\n"):
        Monkey(monkey, 1)

    for r in range(10000):
        for monkey in Monkey.gang:
            monkey.turn()

    actives = sorted([monkey.inspections for monkey in Monkey.gang])
    business = actives[-1] * actives[-2]
    print(business)


if __name__ == "__main__":
    part1()
    Monkey.Reset()
    part2()
