class Solution(object):
    def reflect(self, n):
        new_bin = bin(n)[2:]
        rev_bin = new_bin[::-1]
        return int(rev_bin, 2)
    def sortByReflection(self, nums):
    
        pairs = []
        for i in nums:
            pairs.append((self.reflect(i), i))
        pairs.sort()
        res = []
        for x in pairs:
            res.append(x[1])

        return res   


        