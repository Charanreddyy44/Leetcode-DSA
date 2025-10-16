class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            if i % 2 == 0:
                result.append(0)
            else:
                result.append(1)
            result = sorted(result)
        return result    
