def load(name, fpath):
    import os, imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))

coroutine = load('coroutine', '../part1/coroutine.py')
from coroutine import coroutine

# object
class GrepHandler(object):
    def __init__(self, pattern, target):
        self.pattern = pattern
        self.target = target

    def send(self, line):
        if self.pattern in line:
            self.target.send(line)

# coroutine
@coroutine
def grep(pattern, target):
    while True:
        line = (yield)
        if pattern in line:
            target.send(line)

@coroutine
def null():
    while True:
        item = (yield)

# benchmark
line = 'python is nice'
p1 = grep('python', null())
p2 = GrepHandler('python', null())

from timeit import timeit

print "coroutine:", timeit("p1.send(line)", "from __main__ import line, p1")
print "object:", timeit("p2.send(line)", "from __main__ import line, p2")
