class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dnum = 0
        for num in nums:
            if (dnum >> num) & 1:   
                return num
            dnum |= (1 << num)      
        return -1