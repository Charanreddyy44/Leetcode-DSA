class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        new_bits = []
        while i < len(bits):
            if bits[i] == 1:
                i += 1
                new_bits.append(2)
            else:
                new_bits.append(1)
            i+=1
        if new_bits[-1] == 1:
            return True
        else:
            return False    
