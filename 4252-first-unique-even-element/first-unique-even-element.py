class Solution(object):
    def firstUniqueEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for x in nums:
            if x%2 == 0 and nums.count(x) == 1:
                return x
        
        return -1