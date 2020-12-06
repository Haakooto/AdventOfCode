import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time

class IntcodeComputer:
    def __init__(self, array):
        self.array = array
        self.current = 0

    def run(self):
        reached_end = False
        while not reached_end:
            try:
                opcode = str(self.array[self.current])
            except IndexError:
                print("Index Error!")
                print(self.current)
                print(self)
                sys.exit()

            if len(opcode) == 5:
                A = int(opcode[0])
                opcode = opcode[1:]
            else:
                A = 0
            if len(opcode) == 4:
                B = int(opcode[0])
                opcode = opcode[1:]
            else:
                B = 0
            if len(opcode) == 3:
                C = int(opcode[0])
                opcode = opcode[1:]
            else:
                C = 0
            if len(opcode) == 2:
                op = int(opcode)
            if len(opcode) == 1:
                op = int(opcode)
                
            if op == 1:
                self.add(A, B, C)
            elif op == 2:
                self.mul(A, B, C)
            elif op == 3:
                self.inp(A, B, C)
            elif op == 4:
                self.out(A, B, C)
            elif op == 5:
                self.jumpTrue(A, B, C)
            elif op == 6:
                self.jumpFalse(A, B, C)
            elif op == 7:
                self.lessthan(A, B, C)
            elif op == 8:
                self.equal(A, B, C)
            elif op == 99:
                reached_end = True
            else:
                print(f"\nInvalid opcode encountered! {op}")
                print(self.current)
                print(self)
                sys.exit()
        print(f"Program successfully terminated")

    def get_dfs(self, A, B, C):
        if C:
            fir = self.current + 1
        else:
            fir = self.array[self.current + 1]
        
        if B:
            sec = self.current + 2
        else:
            sec = self.array[self.current + 2]

        # if A:
            # print(f"Something wrong in add")
        if A:
            dest = self.current + 3
        else:
            dest = self.array[self.current + 3]

        return dest, fir, sec

    def add(self, A, B, C):
        dest, fir, sec = self.get_dfs(A, B, C)
        self.array[dest] = self.array[fir] + self.array[sec]
        self.current += 4

    def mul(self, A, B, C):
        dest, fir, sec = self.get_dfs(A, B, C)
        self.array[dest] = self.array[fir] * self.array[sec]
        self.current += 4

    def inp(self, A, B, C):
        i = input("What is your input? ")
        self.array[self.array[self.current + 1]] = int(i)
        self.current += 2

    def out(self, A, B, C):
        if C:
            pos = self.current + 1
        else:
            pos = self.array[self.current + 1]
        o = self.array[pos]
        print(o)
        self.current += 2

    def jump(self, A, B, C):
        if not C:
            bol = self.current + 1
        else:
            bol = self.array[self.current + 1]

        if not B:
            move = self.current + 2
        else:
            move = self.array[self.current + 2]

        return bol, move

    def jumpTrue(self, A, B, C):
        bol, move = self.jump(A, B, C)
        
        if bol:
            self.current = move
        else:
            self.current += 3

    def jumpFalse(self, A, B, C):
        bol, move = self.jump(A, B, C)
        
        if not bol:
            self.current = move
        else:
            self.current += 3

    def lessthan(self, A, B, C):
        dest, fir, sec = self.get_dfs(A, B, C)
        if self.array[fir] < self.array[sec]:
            v = 1
        else:
            v = 0
        self.array[dest] = v
        self.current += 4

    def equal(self, A, B, C):
        dest, fir, sec = self.get_dfs(A, B, C)
        if self.array[fir] == self.array[sec]:
            v = 1
        else:
            v = 0
        self.array[dest] = v
        self.current += 4

    def __str__(self):
        return str(self.array)

def test():
    a = "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"
    a = "3,3,1105,-1,9,1101,0,0,12,4,12,99,1"
    a = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
    p = [int(i) for i in a.split(",")]
    p = np.asarray(p)

    r = IntcodeComputer(p)
    r.run()

def main():
    file = open("/home/hakon/Downloads/aoc5.txt", "r")
    program = file.readline().split(",")
    file.close()
    program = [int(i) for i in program]
    program = np.asarray(program)

    result = IntcodeComputer(program)
    result.run()

if __name__ == "__main__":
    test()
    # main()
