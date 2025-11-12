class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        palindromes = []
        count = 0
        for i in range(len(s)):
            for j in range(i+1, len(s) + 1):
                substring = s[i:j]
                if substring == substring[::-1]:
                    count += 1
        return count        
