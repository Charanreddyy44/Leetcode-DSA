class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinct = set(nums)
        for num in nums:
            reverse_num = int(str(num)[::-1])
            distinct.add(reverse_num)

        return len(distinct)