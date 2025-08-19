class Solution:
    def findComplement(self, num: int) -> int:
    #binary = bin(num)
    #    flip = binary[2:]
     #   flipped = 
        result = 0
        power = 0
    
        while num > 0:
    
            bit = num % 2
            flipped_bit = 1 - bit
        
    
            result += flipped_bit * (2 ** power)
        
            num //= 2
            power += 1
    
        return result
