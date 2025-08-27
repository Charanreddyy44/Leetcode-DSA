class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nested_list = []
        for num in range(1<<n):
            subset = []
            for i in range(n):
                if num & (1<<i):
                    subset.append(nums[i])
            nested_list.append(subset)
        return nested_list            

