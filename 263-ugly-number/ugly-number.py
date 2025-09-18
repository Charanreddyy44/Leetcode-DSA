class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        for s in [2,3,5]:
            while n % s == 0:
                n //= s
        return n == 1            