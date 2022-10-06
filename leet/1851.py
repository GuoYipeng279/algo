class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        intervals.sort(key=lambda x:x[0])
        queries.sort()
        events = []
        for i, it in enumerate(intervals):
            events.append((it[0],0,i,it[1]-it[0])) #起始位置，0，编号，长度
        for i, it in enumerate(queries):
            events.append((it,1,i))
        events.sort(key=lambda x:x[0])
        ans = []
        for item in events:
            
        return ans

if __name__ == '__main__':
    S = Solution()
    ans = S.minInterval(intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5])
    print(ans)