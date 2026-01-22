class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if n & 1 == 0:
                ans.append(-1)
            else:
                x = n
                count = 0
                while x%2==1:
                    count+=1
                    x//=2
                ans.append(n -(1 << (count-1)))
        return ans