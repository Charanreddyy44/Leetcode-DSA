class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best = [[-1, -1] for _ in range(10)]
        ans = -1

        for num in nums:
            temp, largest = num, 0
            while temp > 0:
                largest = max(largest, temp % 10)
                temp //= 10
            if num > best[largest][0]:
                best[largest][1] = best[largest][0]
                best[largest][0] = num
            elif num > best[largest][1]:
                best[largest][1] = num

    
            for x, y in best:
                if x != -1 and y != -1:
                    ans = max(ans, x + y)

        return ans