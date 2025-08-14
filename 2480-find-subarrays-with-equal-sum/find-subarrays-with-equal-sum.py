class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for i in range(len(nums) - 1):
            s = nums[i] + nums[i+1]
            if s in seen:
                return True
            seen.add(s)
        return False    

