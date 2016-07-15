a = pow(7, 5)
m = pow(2, 31) - 1
x = 666 # seed


def setseed(s):
    global x
    x = s


def runif01(start, stop):
    global x
    x = a * x % m
    return start + (stop-start)*(x / float(m))

setseed(99)
print runif01(10, 20)
print runif01(10, 20)
print runif01(10, 20)
print runif01(10, 20)
