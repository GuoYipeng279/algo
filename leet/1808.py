class Solution(object):
    def maxNiceDivisors(self, primeFactors):
        """
        :type primeFactors: int
        :rtype: int
        """
        # 思路：把n分配到质因数上，求如何分配能让可能的组合最多
        # 组合数a-1*b-1*c-1*d-1*...减一由于必须是好因子（每个质因子都包含）
        # 且要满足a+b+c+d+...=n
        # 二分搜索分为的组数  # 思路错了
        def func(mi):  # mi为组数
            group = primeFactors//mi  # 缺组被分配数量
            duo = primeFactors - group*mi  # 多1组的数量
            ans = group**(mi-duo)*(group+1)**duo
            return ans
        def bisearch(lo,hi,cond):
            while lo!=hi:
                mi = (lo+hi)//2
                mia = cond(mi)
                mia1 = cond(mi-1) if mi>=2 else 0
                if mia<=mia1:
                    hi = mi
                else:
                    lo = mi+1
            return lo
        maxi = bisearch(1,primeFactors+1,func)-1
        return int(func(maxi)%(1e9+7))
            
if __name__ == '__main__':
    S = Solution()
    ans = S.maxNiceDivisors(50)
    print(ans)



        # def find_max(sta, dir=1, end=None):
        #     if abs(sta-end)<=1:
        #         return func(sta)
        #     step = abs(end-sta)//3
        #     step = 1 if step == 0 else step
        #     last = -2
        #     now = -1
        #     las1 = sta
        #     las2 = sta
        #     while now>=last:
        #         last = now
        #         now = func(sta)
        #         las2 = las1
        #         las1 = sta
        #         sta += dir*step
        #         if (sta-end)*dir>=0:
        #             sta = end-dir
        #             break
        #         # step*=2
        #     return find_max(sta, -dir, las2-dir)
        # maxi = find_max(1,1,primeFactors+1)