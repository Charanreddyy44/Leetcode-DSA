class Solution(object):
    def maxProfit(self, arr):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > min:
                profit = profit + (arr[i] - min)
            min = arr[i]
        return profit    
        
