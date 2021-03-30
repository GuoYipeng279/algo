a1, a2, a3=map(int,input().split())
inp = []
record = a2
for i in range(a3):
    a = input().split()
    inp.append([float(i) for i in a])
#继续跑
rec = [-1 for i in range(a3)]
rec[-1] = a1-inp[-1][0]
start = 0
#预期第x个障碍
for i in range(a3+1):
    k=a3-i-1
    if k==a3-1:#从最后一个障碍前进的预期用时
        rec[k]=a1-inp[-1][0]
    else:
        #从第k个障碍前进，预期用时=距离耗时+成功率*（k+1预期）+失败率*（k+1预期+倒地时间）
        rrr=inp[k+1][0]-inp[k][0]+inp[k+1][1]*rec[k+1]+(1-inp[k+1][1])*(rec[k+1]+inp[k+1][2])
    if k<0:
        start=rrr
    else:rec[k]=rrr
#障碍i摔倒，是否继续跑
#tim已花时间，纪录时间, 当前障碍
def forward(tim, record,i):
    if time+rec[i]>=record:
        return False
    else:return True
#计时，tim是当前时间，i当前障碍
def timing(tim, i):
    if forward(tim,record,i):
