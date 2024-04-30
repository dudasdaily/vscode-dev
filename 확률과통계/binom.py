import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import norm

# A영역 pdf와 B영어 pdf를 그려봐라
# title은 각각 '수학 A영역', '수학 B영역'

a_mean = 53
a_std = 20

b_mean = 57
b_std = 15

x = np.arange(0, 100, 0.1)
y = norm.pdf(x, a_mean, a_std)

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.bar(x,y)
plt.xlabel('X')
plt.ylabel('f(X)')
plt.title('수학 A영역')
plt.show()

y = norm.pdf(x, b_mean, b_std)
plt.bar(x,y)
plt.xlabel('X')
plt.ylabel('f(X)')
plt.title('수학 B영역')
plt.show()
