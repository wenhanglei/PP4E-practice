"optimize with in-place list operations"

class error(Exception): pass

class Stack:
    def __init__(self, start=[]):
        self.stack = []
        for x in start: self.push(x)

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        if not self.stack: raise error('underflow')
        return self.stack.pop()

    def top(self):
        if not self.stack: raise error('underflow')
        return self.stack[-1]

    def empty(self):
        return not self.stack

    def __len__(self):
        return len(self.stack)

    def __getitem__(self, offset):
        return self.stack[offset]

    def __repr__(self):
        return '[Stack:%s]' % self.stack

































