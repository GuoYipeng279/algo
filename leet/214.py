class Solution(object):
    def shortestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        lis = [i for i in range(l)]
        t = s[::-1]
        lis.sort(key=lambda x:t[x:x+(l-x+1)//2])
        print(s)
        print([t[x:x+(l-x+1)//2] for x in lis])
        def bisearch(item, lis, cond):
            lo = 0
            hi = len(lis)
            while lo!=hi:
                mi = (lo+hi)//2
                if cond(item,t[lis[mi]:]):
                    hi = mi
                else:
                    lo = mi+1
            return lo
        ind = bisearch(s,lis,lambda x,y:x<y)
        return ind
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        app = set([i for i in range(l)])
        for i in range(l):
            if s[i] != 

if __name__ == '__main__':
    S = Solution()
    ans = S.shortestPalindrome("aacrercaaa")
    print(ans)