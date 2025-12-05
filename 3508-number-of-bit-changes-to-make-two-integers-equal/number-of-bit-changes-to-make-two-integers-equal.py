class Solution(object):
    def minChanges(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        k ^= n
        cnt = bin(k).count('1')
        k &= n 
        if cnt == bin(k).count('1'):
            return cnt
        else:
            return -1

        