class Solution:
    def smallestNumber(self, n: int) -> int:
        s = n.bit_length()
        x = (1<< s) - 1
        if n == x:
            return n
        else:
            return x 