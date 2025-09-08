class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        xor = 0
        for num in nums:
            xor ^= num
        for i in range(1, n+1):
            xor ^= i
    
    # Step 2: rightmost set bit
        mask = xor & -xor
        a = b = 0
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num
        for i in range(1, n+1):
            if i & mask:
                a ^= i
            else:
                b ^= i
        if nums.count(a) == 2:
            return [a, b]
        else:
            return [b, a]
        