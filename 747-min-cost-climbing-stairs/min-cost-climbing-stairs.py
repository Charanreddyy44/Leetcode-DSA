class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost1 = cost[0]
        cost2 = cost[1]
        for i in range(2, len(cost)):
            #avg = min(cost1, cost2)
            ans = cost[i] + min(cost1, cost2)
            cost1 = cost2
            cost2 = ans
        return min(cost1, cost2)