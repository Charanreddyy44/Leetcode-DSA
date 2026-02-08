class Solution:
    def countMonobit(self, n: int) -> int:
        count = 0
        for i in range(n + 1):
            b = bin(i)[2:]
            if all(bit == b[0]for bit in b):
                count += 1
        return count
        #count = 1
        #num = 1
        #while num <= n:
        #   count += 1
        #    num = (num << 1)| 1
        #return count    