class Solution:
    def findComplement(self, num: int) -> int:
    #Using method
      # binary = bin(num)[2:]
      # flipped = ''.join('1' if b == '0' else '0' for b in binary)
    #return int(flipped, 2) 
        binary = ""
        while num > 0:
            bit = num % 2
            binary = str(bit) + binary
            num //= 2
        binary = binary if binary else "0"
        flip = ''
        for bit in binary:
            flip += '1' if bit == '0' else '0'
        return int(flip, 2)
