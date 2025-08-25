class Solution(object):
    def countPrimeSetBits(self, left, right):
        
        prime_set = {2, 3, 5, 7, 11, 13, 17, 19}

        count = 0
        
        for num in range(left, right + 1):
            set_bits = bin(num).count('1')
            if set_bits in prime_set:
                count += 1
        return count    