def bisearch(judge, lo, hi):
    while lo!=hi:
        mi = (lo+hi)//2
        if judge(mi):
            hi = mi
        else:
            lo = mi+1
    return lo


class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        for t in tasks:
            t[1] = max(t[0],t[1])
        tasks.sort(key=lambda t:(t[0]-t[1])*1e5-t[1])
        def judge(energy):
            for t in tasks:
                if energy<t[1]:
                    return False
                else:
                    energy-=t[0]
            return True
        lo = sum([t[0] for t in tasks])
        hi = sum([t[1] for t in tasks])
        ans = bisearch(judge,lo,hi)
        return ans


if __name__ == '__main__':
    S = Solution()
    A = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
    ans = S.minimumEffort(A)
    print(ans)