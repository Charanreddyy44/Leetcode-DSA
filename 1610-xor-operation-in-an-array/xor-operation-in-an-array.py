class Solution(object):
    def xorOperation(self, n, start):
        XOR_value = 0
        for i in range(n):
            nums = [start+ i *2]
            for i in nums:

                XOR_value = XOR_value ^ i
        return XOR_value
