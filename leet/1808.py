class Solution(object):
    def maxNiceDivisors(self, primeFactors):
        """
        :type primeFactors: int
        :rtype: int
        """
        # 思路：把n分配到质因数上，求如何分配能让可能的组合最多
        # 组合数a-1*b-1*c-1*d-1*...减一由于必须是好因子（每个质因子都包含）
        # 且要满足a+b+c+d+...=n
        # 二分搜索分为的组数
        maxi = 0
        def find_max(sta):
            step = sta//2
            lo = 0
            hi = None
            while step > 1:
                mi = sta+step
                group = primeFactors//mi  # 缺组被分配数量
                duo = primeFactors - group*mi  # 多1组的数量
                ans = (mi-duo)**(group-1)*(duo)**group
                if ans > maxi:
                    if step>0:
                        lo = sta
                        if hi:
                            step = (hi-mi)//2
                        else:
                            step*=2
                    if step<0:
                        hi = sta
                        step = (lo-mi)//2
            