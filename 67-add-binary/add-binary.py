class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x = int(a, 2)
        y = int(b, 2)

    # Bit manipulation addition
        while y != 0:
            carry = x & y          # common set bits → carry
            x = x ^ y              # sum without carry
            y = carry << 1         # shift carry left

        return bin(x)[2:]