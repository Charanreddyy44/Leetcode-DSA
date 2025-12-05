class Solution(object):
    def findKOr(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        for i in range(32):
            count = 0
            for num in nums:
                if (num >> i) & 1:
                    count += 1
            if count >= k:
                res |= (1 << i)
        return res            
