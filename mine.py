lst = [['-', '*', '-', '-', '-'],
       ['-', '-', '-', '*', '-'],
       ['-', '*', '-', '-', '-'],
       ['-', '-', '-', '-', '-']]

row = 4
col = 5

def count_mine(lst, i, j):
    cnt = 0

    if lst[i][j] == "*":
        return "*"
    
    for m in range(i - 1, i + 2):
        for n in range(j - 1, j + 2):
            if (0 <= m < row) and (0 <= n < col) and (lst[m][n] == "*"):
                cnt += 1
        
    return cnt

for i in range(row):
    for j in range(col):
        lst[i][j] = count_mine(lst, i, j)

print(lst)
