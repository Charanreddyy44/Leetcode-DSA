class Solution(object):
    def maxProfit(self, arr):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min = arr[0]
        for i in range(1, len(arr)):
            profit = max(profit, arr[i] - min)
            if arr[i] < min:
                min = arr[i]
        return profit 

