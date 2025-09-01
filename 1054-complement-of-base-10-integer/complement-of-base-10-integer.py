class Solution(object):
    def bitwiseComplement(self, n):
        if n == 0:
            return 1
        bit_len = n.bit_length()
        comp = (1 << bit_len) - 1
        return comp ^ n        