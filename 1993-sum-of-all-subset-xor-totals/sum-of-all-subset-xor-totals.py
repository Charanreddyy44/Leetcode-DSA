class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subsets = [0]
        Sum = 0 
        for num in nums:
            new_subset = []
            for s in subsets:
                new_XOR = s ^ num
                new_subset.append(new_XOR)
                Sum += new_XOR
            subsets += new_subset
        return Sum



