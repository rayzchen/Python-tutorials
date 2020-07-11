def range(*args):
    if len(args) == 1:
        start = 0
        stop = args[0]
        step = 1
    elif len(args) == 2:
        start, stop = args
        step = 1
    elif len(args) == 3:
        start, stop, step = args
    l = []
    i = start
    while i < stop:
        l.append(i)
        i += step
    return l

def myFunction(**kwargs):
    print(kwargs)