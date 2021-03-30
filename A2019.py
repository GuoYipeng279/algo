n, w = map(int, input().split())
inp = []
for i in range(w):
    inp.append(input().split())
# n = 3
# w = 2
# inp = [[2,1,2],[2,1,3]]
rec = [0 for i in range(n)]
ran = [1]
avg = [0 for i in range(n)]
for i in inp:
    for j in i[1:]:
        j = int(j)
        ori = rec[j-1]
        new = rec[j-1]+1
        rec[j-1] += 1
        ran[ori] += 1
        if len(ran) == new:
            ran.append(1)
    for j in range(n):
        avg[j] += ran[rec[j]]/w
for i in avg:
    print(i)
