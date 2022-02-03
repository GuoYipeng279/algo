import numpy as np
from matplotlib import pyplot as plt
import math
from time import time

def bisearch(item, nums, cond, lo=None, up=None):
    '''
    find the min index i that cond(item, nums[i]) is true
    '''
    lo = 0 if lo is None else lo
    up = len(nums) if up is None else up
    while lo!=up and lo<len(nums):
        mi = lo+(up-lo)//2
        # mi = (up+lo)//2
        if cond(item, nums[mi]):
            up = mi
        else:
            lo = mi+1
    return up

        
class Solution(object):
    def sumOfFlooredPairs_Brute(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l = len(nums)
        otp = np.zeros((l,l))
        for i in range(l):
            for j in range(l):
                otp[i,j] = math.floor(nums[i]/nums[j])
        # plt.imshow(otp, cmap='gray')
        # plt.show()
        return sum(sum(otp))

    def sumOfFlooredPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l = len(nums)
        outcome = 0
        las = [l for _ in range(nums[-1]//nums[0]+1)]
        for i in range(l-1,-1,-1):
            lo = 0
            for j in range(nums[l-1]//nums[i]+1):
                def cond(item, at):
                    return at/item >= j+1
                index = bisearch(nums[i],nums,cond,lo,las[j])
                las[j] = index
                outcome += j*(index-lo)
                lo = index
        return int(outcome%(1e9+7))
            
        

if __name__ == '__main__':
    S = Solution()
    A = [1,3,4,6,7,7,7,9,11,16]
    B = [7,7,7,7,7,7,7]
    C = [i for i in range(1,5000)]
    sta = time()
    print(S.sumOfFlooredPairs_Brute(C))
    print(time()-sta)
    sta = time()
    print(S.sumOfFlooredPairs(C))
    print(time()-sta)