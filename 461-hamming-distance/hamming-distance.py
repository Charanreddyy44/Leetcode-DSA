class Solution(object):
    def hammingDistance(self, x, y):
        k = x^y
        c = 0
        while k:
            if k&1 == 1:
                c+=1
            k>>=1
        return c        
        