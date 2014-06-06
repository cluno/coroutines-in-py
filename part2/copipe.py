def load(name, fpath):
    import os, imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))

coroutine = load('coroutine', '../part1/coroutine.py')
from coroutine import coroutine

import time
def follow(thefile, target):
    print 'invoke follow'
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)

# A filter
@coroutine
def grep(pattern, target):
    while True:
        print 'waiting in grep'
        line = (yield)
        if pattern in line:
            target.send(line)

# A sink
@coroutine
def printer():
    while True:
        print 'waiting in printer'
        line = (yield)
        print line

if __name__ == '__main__':
    f = open('/var/log/system.log')
    follow(f,
            grep('kernel',
            printer()))
