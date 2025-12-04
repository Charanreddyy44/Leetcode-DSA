class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = nums[-2]
        j = nums[-1]
        return (i - 1)*(j - 1)
