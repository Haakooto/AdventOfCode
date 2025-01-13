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
        rs, p = file.read().split("\n\n")
    regs = [int(i) for i in re.findall(r"\d+", rs)]
    prog = [int(i) for i in re.findall(r"\d+", p)]
    return regs, prog

def ERROR():
    assert False, "Combo value 7 used, program invalid"

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
        3: lambda op: None,  # Jump-op, do nothing when A == 0
    }

    pointer = 0
    while pointer < len(program):
        inst = program[pointer]
        op = program[pointer + 1]
        if inst == 3 and register.A() != 0:  # jump
            pointer = op - 2  
        elif inst == 5:  # output
            yield combo[op]() % 8 
        else:  # all other actions
            instructions[inst](op) 
        pointer += 2

def solver1_alt3(input_file):
    register, program = read(input_file)
    return ",".join([str(o) for o in run_opcode(program, register)])

def solver2_alt3(input_file):
    register, program = read(input_file)
    As = range(2**7)  # prog uses up to 10 bits per output, get rest 3 from loop below (range 8)
    for k, p in enumerate(program):
        candidates = []
        for i in range(8):  # loop over all 3-bit numbers
            v = (i + 1) * 2**(7 + k*3)  # Add to start of binary number
            # v look like bbb00000... where bbb in bin(0 - 8), and 7 + 3k zeros
            for j in As:  # loop over prev candidates
                register[0] = j + v
                g = run_opcode(program, register)
                for _ in range(k): 
                    next(g)  # assume first k outputs are correct
                if next(g) == p:
                    candidates.append(j + v)
        # Above loop find candidates based on first some bits
        # Check if any candidates solves exactly
        for A in candidates:
            sols = []
            register[0] = A
            ns = [i for i in run_opcode(program, register)]
            if ns == program:
                sols.append(A)
            if sols:
                return min(sols)
        As = candidates
