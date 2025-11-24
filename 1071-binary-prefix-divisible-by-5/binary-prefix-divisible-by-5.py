class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        x = 0
        for v in nums:
            x = (x*2 + v) % 5
            res.append(x == 0)
        return res    
