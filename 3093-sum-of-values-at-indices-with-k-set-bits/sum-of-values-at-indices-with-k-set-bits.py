class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        for i, val in enumerate(nums):
            cnt = 0
            n = i
            while n > 0:       
                if n & 1:       
                    cnt += 1
                n >>= 1         
            if cnt == k:
                total += val
        return total