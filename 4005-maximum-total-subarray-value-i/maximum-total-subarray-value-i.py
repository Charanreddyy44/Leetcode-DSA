class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = nums
        max_val = max(res)
        min_val = min(res)
        return k*(max_val - min_val)
        