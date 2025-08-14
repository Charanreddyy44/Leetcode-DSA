class Solution(object):
    def largestGoodInteger(self, num):  
        for i in range(9, -1, -1):
            s = str(i) * 3
            if s in num:
                return s
        return ""