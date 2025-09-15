class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev = n & 1  # last bit
        n >>= 1
        while n > 0:
            curr = n & 1
            if curr == prev:   # two equal adjacent bits found
                return False
            prev = curr
            n >>= 1
        return True
        