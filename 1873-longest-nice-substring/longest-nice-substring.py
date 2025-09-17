class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2: 
            return ""
        char = set(s)
        for i, ch in enumerate(s):
            if ch.swapcase() not in char:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                if len(left) >= len(right):
                    return left
                else:
                    return right
        
        return s    