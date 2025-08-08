class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums_map = {}
        max_sum = -1
    
        for num in nums:
            s = 0
            temp = num
            while temp:
                s += temp % 10
                temp //= 10
        
            if s in sums_map:
                max_sum = max(max_sum, sums_map[s] + num)
                if num > sums_map[s]:
                    sums_map[s] = num
            else:
                sums_map[s] = num
    
        return max_sum