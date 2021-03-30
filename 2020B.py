n = int(input())
r = input().split()
r = [int(i) for i in r]
m = int(input())
inp = []
for i in range(m):
    a, b, c = map(int, input().split())
    inp.append([a,b,c])
table = []
for i, j in r:
    table.append((i,j,i+j))
table = dict(table)
