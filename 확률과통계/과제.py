import numpy as np

a = np.array([10,2,3,3,7,7,7,7,1,4])
a.sort() # equal with a = np.sort(a)

def joongang(a):
    if a.size == 0:
        print('there is no element in array.')
        return None

    if a.size % 2 == 0: # 리스트가 짝수일 때
        return (a[a.size // 2] + a[a.size // 2 - 1]) / 2
    
    else: # 리스트가 홀수일 떄
        return a[a.size // 2]
    
print(joongang(a))
