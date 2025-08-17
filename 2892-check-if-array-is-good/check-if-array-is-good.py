class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = max(nums)
        if len(nums)!= n+1:
            return False
        for i in range(1, n):
            if nums.count(i) != 1:
                return False
        if nums.count(n) != 2:
            return False
        return True                