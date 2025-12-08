class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """

        return (high+1) // 2 - (low // 2)
       # count = 0
       # for i in range(low, high+1):
        #    if i % 2 == 1:
        #        count += 1
        # return count
