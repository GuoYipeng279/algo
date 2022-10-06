from heapq import heapify


class Solution(object):
    def minimumIncompatibility(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l = len(nums)
        lis = []
        for i in range(l):
            for j in range(l):
                if nums[i] != nums[j]:
                    lis.append((abs(nums[i]-nums[j]),i,j))
        heapify(lis)

        