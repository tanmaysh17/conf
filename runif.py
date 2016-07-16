a = pow(7, 5)
m = pow(2, 31) - 1
x = 666 # seed


def setseed(s):
    global x
    x = s


def runif01(start, stop, seed):
    setseed(seed)
    global x
    x = a * x % m
    return int(start + (stop-start)*(x / float(m)))

