class Solution(object):
    def hammingDistance(self, x, y):

        k = x^y 
        count = 0 
        while k: 
            if k&1 == 1:
                count+=1
            k>>=1
        return count
        