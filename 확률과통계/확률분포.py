import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# When roll the dice 3 times, if result is multiple of 3, regard as success
# number of success is X, submit mean, variance, and probabilty of each X 
n = 3 # trial number
p = 1/3 # probality of success

x = np.arange(n + 1) # [0 1 2 3]

prob = binom.pmf(x, n, p)

plt.bar(x, prob)
plt.xlabel('Number of Success')
plt.ylabel('Probability')

plt.show()