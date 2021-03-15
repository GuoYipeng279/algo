import numpy as np
n = int(input())
lst = []
for i in range(n):
    x, y = map(int, input().split())
    lst.append([x, y])
lst = np.mat(lst)
totx = []
toty = []
back = 0
last = 0
for i in range(n):
    back += last-lst[i, 0]
    totx.append(back**2)
back = 0
last = 0
for i in range(n):
    back += last-lst[i, 1]
    toty.append(back**2)
tot = sum(totx)+sum(toty)
print(tot)
