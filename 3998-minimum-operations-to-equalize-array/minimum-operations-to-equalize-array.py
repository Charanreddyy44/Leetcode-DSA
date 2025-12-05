class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = nums.count(nums[0])

        if cnt < len(nums):
            return 1
        else:
            return 0