class Solution(object):
    def countPrimeSetBits(self, left, right):
        def is_prime(n):
            return n in {2, 3, 5, 7, 11, 13, 17, 19}

        def count_set_bits(n):
            count = 0
            while n>0:
                if n&1:
                    count +=1
                n = n >> 1   
            return count

        total = 0
        for num in range(left, right + 1):
            set_bits = count_set_bits(num)
            if is_prime(set_bits):
                total += 1
        return total  
          
       # USING METHOD
        #prime_set = {2, 3, 5, 7, 11, 13, 17, 19}
        #count = 0
        #for num in range(left, right + 1):
         #   set_bits = bin(num).count('1')
         #  if set_bits in prime_set:
         #     count += 1
        #return count    