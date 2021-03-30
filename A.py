n = int(input())
xx, yy = [], []
for i in range(n):
    x, y = map(int, input().split())
    xx.append(x)
    yy.append(y)
xx = [[i, 1] for i in xx]


def sumi(xx):
    cut = [0]
    end = []
    for i in range(1, n):
        if xx[i][0] > xx[i-1][0]:
            cut.append(i)  # 切割点
            end.append(i)
    if len(end) == 0:
        return xx
    end.append(n)
    new = []
    for i, j in zip(cut, end):
        new.append([sum(xx[i:j][0])/sum(xx[i:j][1]), sum(xx[i:j][1])])
    return sumi(new)


def solve(xx, mm):
    otp = 0
    for i, j in zip(xx, mm):
        otp += (i-j)**2
    return otp

print(sumi(xx))
print(solve(xx, sumi(xx))+solve(yy, sumi(yy)))
