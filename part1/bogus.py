def countdown(n):
    print "Counting down from", n
    while n >= 0:
        newvalue = (yield n)
        # If a new value got sent in, reset n with it
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1

if __name__ == '__main__':
    c = countdown(5)
    for x in c:
        print x
        if x == 5:
            c.send(3)