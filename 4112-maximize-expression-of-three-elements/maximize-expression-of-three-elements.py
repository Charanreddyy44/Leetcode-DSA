class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[-1]
        b = nums[-2]
        c = min(nums)
        return a+b-c