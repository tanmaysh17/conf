import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math

TRIALS = 20

def sample(data):

    global TRIALS
    sample = []
    X_ = []
    inside = []

    for i in range(0, TRIALS):

        for j in range(0, len(data)):
            sample_indice = np.random.randint(0, len(data))
            sample.append(data[sample_indice])

        X_.append(np.mean(sample))

    X_ = sorted(X_)
    for k in range(int(TRIALS*0.025), int(TRIALS*0.975)):
        inside.append(X_[k])

    print inside[0], inside[-1]
    print X_
    return X_, inside


def normpdf(x, mu, sigma):
    out = [0]*len(x)
    for i in range(0, len(x)):
        a = 1/(sigma*math.sqrt(2*math.pi))
        b = math.exp(-1*pow((x[i]-mu), 2)/(2*pow(sigma, 2)))
        out[i] = a*b
    return out


prices = []
f = open('prices.txt')

for line in f:
    v = float(line.strip())
    prices.append(v)

sample_means, confidence = sample(prices)


plt.axis([1.10, 1.201, 0, 30])
x = np.arange(1.05, 1.25, 0.001)
y = stats.norm.pdf(x, np.mean(prices), np.std(prices)/pow(len(prices), 0.5))
plt.plot(x, y, color = 'red')

plt.plot(confidence[0], 0, 'g^', confidence[-1], 0, 'g^')

mean = np.mean(prices)
stddev = np.std(prices)/pow(len(prices), 0.5)
left = mean - 2*stddev
right = mean + 2*stddev

ci_x = np.arange(left, right, 0.001)
ci_y = normpdf(ci_x, mean, stddev)


plt.fill_between(ci_x, ci_y, color = '#F8ECE0')
fig = plt.figure()
ax = fig.add_subplot(111)

plt.text(.02, .95, '$TRIALS = %d$' % TRIALS, transform = ax.transAxes)
plt.show()

