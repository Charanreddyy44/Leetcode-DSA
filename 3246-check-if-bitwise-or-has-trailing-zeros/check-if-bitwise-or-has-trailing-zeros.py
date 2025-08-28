class Solution(object):
    def hasTrailingZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        even_count = 0
        for num in nums:
            if (num & 1) == 0:  
                even_count += 1
                if even_count >= 2:
                    return True
        return False