l, q = map(int, input().split())
a = input().split()
inp = [int(i) for i in a]
for i in range(l,2*l+1):
    mi = 2147483647
    for j in range(0,i):
        k=i-j-1
        mi = min(mi,inp[k]+inp[j])
    inp.append(mi)
period = inp[l:2*l]
diff = inp[2*l]-inp[l]
lst= []
for i in range(q):
    nn = int(input())
    if nn < l:print(inp[nn])
    else:print(diff*(nn//l)+period[nn%l])