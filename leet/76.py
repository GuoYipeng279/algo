class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """ 
        def toint(c):
            it = ord(c)-97
            if it < 0:
                it = ord(c)-65+26
            return it
        lis = [0 for i in range(52)]
        for c in t:
            it = toint(c)
            lis[it] += 1
        mini = 1e10
        cont = [0 for i in range(52)]
        lo = 0
        rec = [0,0]
        have = False
        for i in range(len(s)):
            it = toint(s[i])
            was = cont[it]-lis[it]
            cont[it] += 1
            if have or (was<0 and cont[it]-lis[it]>=0) and min([cont[j]-lis[j] for j in range(52)])>=0:
                have = True
                while cont[toint(s[lo])]-lis[toint(s[lo])]>=1:
                    cont[toint(s[lo])] -= 1
                    lo+=1
                if i-lo+1<mini:
                    rec = [lo,i+1]
                    mini = i-lo+1
        return s[rec[0]:rec[1]]

if __name__ == '__main__':
    S = Solution()
    ans = S.minWindow(s = "ab", t = "a")
    print(ans)