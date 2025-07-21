class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum = 0
        product = 1
        temp = n

        while temp > 0:
            digit = temp % 10
            sum += digit
            product *= digit
            temp //= 10

        total = sum + product
        
        return n % total == 0