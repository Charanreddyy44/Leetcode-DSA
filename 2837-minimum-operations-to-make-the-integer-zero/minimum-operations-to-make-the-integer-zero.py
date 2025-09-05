class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        def popcount(x):
            cnt = 0
            while x:
                x &= x - 1   
                cnt += 1
            return cnt

        for k in range(1, 61):
            target = num1 - k * num2
            if target >= k and popcount(target) <= k:
                return k
        return -1