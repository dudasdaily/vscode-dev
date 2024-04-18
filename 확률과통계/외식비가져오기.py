import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

price = pd.read_csv("확률과통계/samples/외식비/외식비.csv")

a = np.array(stats.skew(price))
a = np.round(a, 3)

print(a)
# print(stats.kurtosis(price))


plt.hist(price.냉면, bins = 5, label = 'nangmun')
plt.legend()
plt.show()
plt.hist(price.비빔밥, bins = 5, label = 'bibimbap', color = 'black')
plt.legend()
plt.show()
plt.hist(price.김치찌개, bins = 5, label = 'gimchiccigae', color = 'gold')
plt.legend()
plt.show()
plt.hist(price.삼겹살, bins = 5, label = 'samgupsal', color = 'lime')
plt.legend()
plt.show()
plt.hist(price.자장면, bins = 5, label = 'jjajangmun', color = 'navy')
plt.legend()
plt.show()
plt.hist(price.삼계탕, bins = 5, label = 'samgaetang', color = 'red')
plt.legend()
plt.show()
plt.hist(price.칼국수, bins = 5, label = 'kalguksu', color = 'teal')
plt.legend()
plt.show()
plt.hist(price.김밥, bins = 5, label = 'gimbap', color = 'crimson')
plt.legend()
plt.show()

'''  
삼계탕 : -0.724
김밥 : -0.128
칼국수 : -0.048
삼겹살 :  0.04
냉면 : 0.162
자장면 : 0.168
비빔밥 : 0.612
김치찌개 : 1.003
'''