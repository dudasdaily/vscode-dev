import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1장 8번
# fish = np.array([2,3,3,4,4,4,4,5,5,6])
# print("합 : ", fish.sum(), np.sum(fish))
# print("개수 : ", fish.size, np.size(fish))
# print("평균 : ", fish.mean(), np.mean(fish))

#1장 9번
# a = np.zeros(5, dtype=int)
# print(a)
# a = np.zeros((3,3), dtype=int)
# print(a)
# a = np.ones(5)
# print(a)

#1장 10번
# a = np.tile(3, 7)
# print(a)
# a = np.full(3, 7)
# print(a)
# a = np.eye(3, dtype=int)
# print(a)

#1장 11번
# a = np.arange(0,20)
# print(a.reshape(4,5))

#1장 12번
# a = [1, 'A']
# print(type(a[0]))
# print(type(a[1]))

# a = np.array(a)
# print(type(a[0]))
# print(type(a[1]))

#1장 13번
# df1 = pd.DataFrame({
#     'a' : [1,2,3],
#     'b' : [4,5,6]
# })

# df2 = pd.DataFrame({
#     'a' : [7,8,9],
#     'b' : [10,11,12]
# })

# cc = pd.concat([df1, df2], axis=0)
# cc = pd.concat([df1, df2], axis=1)
# print(cc)

#1장 14번
# a = pd.DataFrame(
#     [['A', 1],
#      ['B', 2],
#      ['C', 3]],
#      columns=['x1', 'x2']
# )

# b = pd.DataFrame({
#     'x1' : ['B', 'C', 'D'],
#     'x3' : [2, 3, 4]
# })

# print(pd.concat([a, b]), "\n")
# print(pd.concat([a, b], axis=1), "\n")

#15
# a = np.array([2,3,3,4,4,4,4,5,5,6])
# print(a.var())
# print(a.var(ddof=1))

#16
