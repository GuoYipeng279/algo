class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nfac = [1]
        for i in range(n):
            nfac.append(nfac[-1]*(i+1))
        kk = k-1
        anwe = []
        for i in range(n+1):
            kn = nfac[n-i]
            anwe.append(kk//kn)
            kk = kk%kn
        have = [i for i in range(1,n+1)]
        tore = []
        for i in range(n):
            lis = []
            for j in have:
                if j is not None:
                    lis.append(j)
            tore.append(str(lis[anwe[i+1]]))
            have[lis[anwe[i+1]]-1] = None
        return ''.join(tore)
        
if __name__ == '__main__':
    S = Solution()
    ans = S.getPermutation(7,3)
    print(ans)