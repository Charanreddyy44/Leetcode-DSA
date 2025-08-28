class Solution(object):
    def hasTrailingZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        even_count = 0
        for num in nums:
            if (num & 1) == 0:  # check if last bit is 0 (even)
                even_count += 1
                if even_count >= 2:  # found 2 evens, enough
                    return True
        return False