class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        nested_list = []
        duplicate = set()
        for num in range (1<<n):
            subset = []
            for i in range(n):
                if num & (1<<i):
                    subset.append(nums[i])
            duplicate.add(tuple(subset))
        return [list(s) for s in duplicate]