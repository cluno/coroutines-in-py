def countdown(n):
    m = n + 5
    print "Counting down from", n, m
    while n > 0:
        yield n
        yield m
        n -= 1
        m += 1
    print "Done counting down"

if __name__ == '__main__':
    for i in countdown(10):
        print i