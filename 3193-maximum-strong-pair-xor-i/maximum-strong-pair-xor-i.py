class Solution(object):
    def maximumStrongPairXor(self, nums):
        
        n = len(nums)
        max_XOR = 0
        for i in range(n):
            for j in range(i, n):
                x = nums[i]
                y = nums[j]
                if abs(x-y) <= min(x, y):
                    max_XOR = max(max_XOR, x^y)
        return max_XOR         