class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        XOR_all = 0
        XOR_nums = 0

        for i in range(n + 1):  
            XOR_all ^= i

        for num in nums:       
            XOR_nums ^= num

        return XOR_all ^ XOR_nums