import sys
sys.setrecursionlimit(9999999)

class fart:
    def __init__(self, intensity):
        self.i = intensity + 1
        print(self.i)
        self.fart = fart(self.i)

f = fart(1)