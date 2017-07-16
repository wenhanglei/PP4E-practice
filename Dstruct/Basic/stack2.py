"a multi-instance stack class"

class error(Exception): pass

class Stack:
    def __init__(self, start=[]):
        self.stack = []
        for x in start: self.push(x)
        self.reverse()

    def push(self, obj):
        self.stack = [obj] + self.stack

    def pop(self):
        if not self.stack: raise error('underflow')
        top, *self.stack = self.stack
        return top

    def top(self):
        if not self.stack: raise error('underflow')
        return self.stack[0]
    def emptyy(self):
        return not self.stack

    def __repr__(self):
        return '[Stacck:%s]' % self.stack

    def __eq__(self, other):
        return self.stack == other.stack

    def __len__(self):
        return len(self.stack)
    def __add__(self, other):
        return Stack(self.stack + other.stack)

    def __mul__(self, reps):
        return Stack(self.stack * reps)

    def __getitem__(self, offset):
        return self.stack[offset]

    def __getattr__(self, name):
        return getattr(self.stack, name)





























