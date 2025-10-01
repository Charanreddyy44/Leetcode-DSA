class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total = numBottles
        while numBottles >= numExchange:
            numBottles -= numExchange -1
            total +=1
        return total 