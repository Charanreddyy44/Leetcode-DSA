class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import Counter
        count = Counter(nums)
        for freq in count.values():
            if freq >2:
                return False
            
        return True    