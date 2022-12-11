import numpy as np

class Register:
    def __init__(self):
        self.X = 1
        self._cycle = 0
        self.strength = 0
        self.length = 40
        self.lines = 6
        self.screen = np.zeros(self.length * self.lines)

    def noop(self):
        self.cycle()

    def add(self, v):
        self.cycle()
        self.cycle()
        self.X += v

    def cycle(self):
        if abs(self._cycle % self.length - self.X) <= 1:
            self.screen[self._cycle] = 1

        self._cycle += 1
        if (self._cycle - 20) % self.length == 0:
            self.strength += self._cycle * self.X

    def render(self):
        for line in self.screen.reshape((self.lines, self.length)):
            print("".join(np.where(line, "#", ".")))


RegX = Register()
for line in open("input").read().strip().split("\n"):
    if (line:=line.split(" "))[0] == "noop":
        RegX.noop()
    else:
        RegX.add(int(line[1]))

print(RegX.strength)
RegX.render()