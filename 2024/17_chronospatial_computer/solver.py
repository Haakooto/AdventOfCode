import re
from types import SimpleNamespace

class Register:
    def __init__(self, v):
        self.val = v

    def __call__(self, new=None):
        if new is None:
            return self.val
        self.val = new


def read(file):
    with open(file, "r") as file:
        c = file.read()
    rs, p = c.split("\n\n")
    regs = [int(i) for i in re.findall(r"\d+", rs)]
    prog = [int(i) for i in re.findall(r"\d+", p)]
    return regs, prog

def ERROR():
    assert False, "Combo value 7 used!"

def run_opcode(program: list[int], register: list[int]):
    register = {c: Register(i) for c, i in zip("ABC", register)}
    register = SimpleNamespace(**register)

    combo = {
        0: lambda: 0,
        1: lambda: 1,
        2: lambda: 2,
        3: lambda: 3,
        4: register.A,
        5: register.B,
        6: register.C,
        7: ERROR,
    }
    def divider(op):
        return int(register.A() / (2 ** combo[op]()))
    instructions = {
        0: lambda op: register.A(divider(op)),
        6: lambda op: register.B(divider(op)),
        7: lambda op: register.C(divider(op)),
        1: lambda op: register.B(register.B() ^ op),
        2: lambda op: register.B(combo[op]() % 8),
        4: lambda op: register.B(register.B() ^ register.C()),
        3: lambda op: None,  # In case inst is 3 and A is 0
    }

    pointer = 0
    while pointer < len(program):
        inst = program[pointer]
        op = program[pointer + 1]
        if inst == 3 and register.A() != 0:
            pointer = op - 2  # reset pointer
        elif inst == 5:
            yield combo[op]() % 8  # output
        else:
            instructions[inst](op)  # other actions
        pointer += 2

def solver1_alt3(input_file):
    register, program = read(input_file)
    output = []

    for o in run_opcode(program, register):
        output.append(str(o))

    return ",".join(output)

def solver2_alt3(input_file):
    register, program = read(input_file)
    As = range(2**7)  # prog uses up to 10 bits per output, get rest 3 from loop below (range 8)
    for k, p in enumerate(program):
        A2 = []
        for i in range(8):
            v = (i + 1) * 2**(7 + k*3)  # adds 7+3k 0s to binary rep.
            for j in As:
                register[0] = j + v
                g = run_opcode(program, register)
                for _ in range(k):
                    next(g)
                if next(g) == p:
                    A2.append(j + v)
        # Above loop find candidates based on first some bits
        # Check if any candidates solves exactly
        for a in A2:
            sols = []
            register[0] = a
            ns = [i for i in run_opcode(program, register)]
            if ns == program:
                sols.append(a)
            if sols:
                return min(sols)
        As = A2
