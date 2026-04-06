class Solution(object):
    def firstMatchingIndex(self, s):
        """
        :type s: str
        :rtype: int
        """
        k = len(s)
        for i in range(k):
            if s[i] == s[k-i-1]:
                return i
        return -1

