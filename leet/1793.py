class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = len(nums)
        nums.append(0)
        left = [-1 for i in range(nums[k]+1)]
        mini = nums[k]
        for i in range(k,-2,-1):
            if nums[i] >= mini: # 当左值大于当前最小
                nums[i] = mini  # 左侧降序
            else:  #左值小于当前最小
                for j in range(nums[i]+1,mini+1):
                    left[j] = i+1
                mini = nums[i]
        mini = nums[k]
        right = [-1 for i in range(nums[k]+1)]
        for i in range(k,l+1):
            if nums[i] >= mini:
                nums[i] = mini  # 右侧降序
            else:
                for j in range(nums[i]+1,mini+1):
                    right[j] = i-1
                mini = nums[i]
        maxi = 0
        for i in range(nums[k]+1):
            maxi = max(maxi,i*(right[i]-left[i]+1))
        return maxi

if __name__ == '__main__':
    S = Solution()
    ans = S.maximumScore(nums = [5,5,4,5,4,1,1,1], k = 0)
    print(ans)
