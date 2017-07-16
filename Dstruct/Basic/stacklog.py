"customize stack for usage data"

from stack2 import Stack

class StackLog(Stack):
    pushes = pops = 0
    def __init__(self, start=[]):
        self.maxlen = 0
        Stack.__init__(self, start)

    def push(self, object):
        Stack.push(self, object)
        StackLog.pushes += 1
        self.maxlen = max(self.maxlen, len(self))

    def pop(self):
        StackLog.pops += 1
        return Stack.pop(self)

    def stats(self):
        return self.maxlen, self.pushes, self.pops




























