### All libraries imported
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math
import sys

### Setting default values for parameters
fancy = False
TRIALS = 500

if len(sys.argv) > 1:
    TRIALS = int(sys.argv[1])
    if len(sys.argv) > 2 and sys.argv[2] == '-fancy':
        fancy = True

def sample(data):   ### Function for bootstrapping

    global TRIALS
    samplen = []
    X_ = []
    inside = []

    for i in range(0, TRIALS):
        samplen = []
        for j in range(0, len(data)):
            sample_indice = np.random.randint(0, len(data))
            samplen.append(data[sample_indice])
        X_.append(np.mean(samplen))

    X_ = sorted(X_)

    for k in range(int(TRIALS*0.025), int(TRIALS*0.975)):
        inside.append(X_[k])

    print inside[0], inside[-1]
    return X_, inside


def normpdf(x, mu, sigma):
    out = [0]*len(x)
    for i in range(0, len(x)):
        a = 1/(sigma*math.sqrt(2*math.pi))
        b = math.exp(-1*pow((x[i]-mu), 2)/(2*pow(sigma, 2)))
        out[i] = a*b
    return out

def graph_fancy():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.text(.02, .95, '$TRIALS = %d$' % TRIALS, transform = ax.transAxes)
    plt.text(.02,.9, '$mean(prices)$ = %f' % np.mean(prices), transform = ax.transAxes)
    plt.text(.02,.85, '$mean(\\overline{X})$ = %f' % np.mean(X_), transform = ax.transAxes)
    plt.text(.02,.80, '$stddev(\\overline{X})$ = %f' %
        np.std(X_,ddof=1), transform = ax.transAxes)
    plt.text(.02,.75, '95%% CI = $%1.2f \\pm 1.96*%1.3f$'%
        (np.mean(X_),np.std(X_,ddof=1)), transform = ax.transAxes)
    plt.text(.02,.70, '95%% CI = ($%1.2f,\\ %1.2f$)' %
                      (np.mean(X_)-1.96*np.std(X_),
                       np.mean(X_)+1.96*np.std(X_)),
             transform = ax.transAxes)
    plt.text(1.135, 11.5, "Expected", fontsize=16)
    plt.text(1.135, 10, "95% CI $\\mu \\pm 1.96\\sigma$", fontsize=16)
    plt.title("95% Confidence Intervals: $\\mu \\pm 1.96\\sigma$", fontsize=16)
    ax.annotate("Empirical 95% CI",
                 xy=(inside[0], .3),
                 xycoords="data",
                 xytext=(1.13,4), textcoords='data',
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3"), fontsize=16)


prices = []
f = open('prices.txt')

for line in f:
    v = float(line.strip())
    prices.append(v)

X_, inside = sample(prices)

if fancy == True:
    graph_fancy()


plt.axis([1.10, 1.201, 0, 30])
x = np.arange(1.05, 1.25, 0.001)
y = stats.norm.pdf(x, np.mean(prices), np.std(prices)/pow(len(prices), 0.5))
plt.plot(x, y, color = 'red')
plt.plot(inside[0], 0, 'g^', inside[-1], 0, 'g^')

mean = np.mean(prices)
stddev = np.std(prices)/pow(len(prices), 0.5)
left = mean - 2*stddev
right = mean + 2*stddev

ci_x = np.arange(left, right, 0.001)
ci_y = normpdf(ci_x, mean, stddev)

plt.fill_between(ci_x, ci_y, color = '#F8ECE0')
plt.savefig('conf -' + str(TRIALS) + ('-basic' if not fancy else '') + '.pdf', format="pdf")
plt.show()

