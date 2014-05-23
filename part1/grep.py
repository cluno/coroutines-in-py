def grep(pattern):
    print "Looking for %s " % pattern
    while True:
        print '> waiting.. ready to receive a value.'
        line = (yield)
        print '> yield done, resuming grep!'
        if pattern in line:
            print line,
        print '> grep done'

if __name__ == '__main__':
    g = grep("python")
    g.next()
    print '> next() invoked'
    g.send("Yeah, but no, but yeah, but no")
    g.send("A series of tubes")
    g.send("python generators rock!")