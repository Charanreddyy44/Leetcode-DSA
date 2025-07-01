class Solution(object):
    def fillCups(self, amount):
        amount.sort()
        total = sum(amount)
        max_cup = amount[2]
        return max(max_cup, (total+1)//2)
        """
        :type amount: List[int]
        :rtype: int
        """
        