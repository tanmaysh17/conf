import numpy as np

TRIALS = 10

def sample(data):

    global TRIALS
    samplen = []
    X_ = []
    inside = []

    for i in range(0, TRIALS):
        sample_indice = np.random.random_integers(0, len(data)-1, 40)
        for j in range(0, 40):
            samplen.append(data[sample_indice[j]])
        print samplen
        X_.append(np.mean(samplen))

    X_ = sorted(X_)

    for k in range(int(TRIALS*0.025), int(TRIALS*0.975)):
        inside.append(X_[k])

    print inside[0], inside[-1]
    return X_, inside


prices = []
f = open('prices.txt')

for line in f:
    v = float(line.strip())
    prices.append(v)

print sample(prices)



