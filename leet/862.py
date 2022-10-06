class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        summ = 0
        l = len(nums)
        for right in range(l):
            summ += nums[right]
            if summ>=k:
                re

if __name__ == '__main__':
    S = Solution()
    ans = S.shortestSubarray([44,-25,75,-50,-38,-42,-32,-6,-40,-47],19)
    print(ans)
