class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_bitwise_and = max(nums)
        currnt_result = 0
        result = 0
        for i in nums:
            if i == max_bitwise_and:
                currnt_result += 1
                result = max(result, currnt_result)
            else:
                currnt_result = 0
        return result             
