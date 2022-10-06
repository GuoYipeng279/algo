class Solution:
    def bisearch_bigger(lis, target,low, high):
        # -1, len(lis)
        while high>low:
            mid = (high+low)//2
            if lis[mid] <target:
                low = mid+1
            elif lis[mid] > target:
                high = mid
            else:
                return mid, True
        return low, lis[low] == target
    def bisearch_smaller(lis, target,low, high):
        while high>low:
            mid = (high+low+1)//2
            if lis[mid] <target:
                low = mid
            elif lis[mid] > target:
                high = mid-1
            else:
                return mid, True
        return high, lis[high] == target
    def searchMatrix(self, matrix, target) -> bool:
        if not matrix or not matrix[0]:
            return False
        rg_low, rg_high = 0, len(matrix[0])-1
        print(rg_low, rg_high)
        for i in range(len(matrix)//2):
            rg_high, b1 = Solution.bisearch_bigger(matrix[i],target,rg_low,rg_high)
            print(rg_low, rg_high)
            rg_low, b2 = Solution.bisearch_smaller(matrix[len(matrix)-1-i],target,rg_low,rg_high)
            print(rg_low, rg_high)
            if b1 or b2: 
                return True
        if len(matrix)%2==1:
            search, find = Solution.bisearch_smaller(matrix[len(matrix)//2],target,rg_low,rg_high)
            return find
        return False

if __name__ == '__main__':
    S = Solution()
    A = [[-1,3]]
    B = -1
    R = S.searchMatrix(A,B)
    print(R)