class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        last_bit = n & 1 
        n >>= 1
        while n > 0:
            currnt = n & 1
            if currnt == last_bit: 
                return False
            last_bit = currnt
            n >>= 1
        return True
        