def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line

if __name__ == '__main__':
    from follow import follow
    logfile = open("/var/log/system.log")
    loglines = follow(logfile)
    pylines = grep("python", loglines)

    for line in pylines:
        print line,