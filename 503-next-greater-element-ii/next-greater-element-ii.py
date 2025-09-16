class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        for i in range(n):
            found = -1
        
            for j in range(1, n+1):
                if nums[(i + j) % n] > nums[i]:
                    found = nums[(i + j) % n]
                    break
            res.append(found)
        return res