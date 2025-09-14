import math
class Solution(object):
    def smallestAbsent(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        avg = sum(nums) / len(nums)       
        s = set(nums)               

        candidate = max(math.floor(avg)+1, 1)       
        while candidate in s:       
            candidate += 1

        return int(candidate)  