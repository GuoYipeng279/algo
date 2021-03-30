n, k = map(int, input().split())
d, s = map(int, input().split())
p = (n*d-k*s)/(n-k)
if p > 100 or p < 0:
    print('impossible')
else:
    print(p)
