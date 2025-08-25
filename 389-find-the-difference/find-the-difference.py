class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for char in s:
            result ^= ord(char)
        for char in t:
            result ^= ord(char)
        return chr(result)      
    #USING SORTING
     #   s = sorted(s)
     #   t = sorted(s)
     #   for i in range(len(s)):
     #       if s[i] != t[i]
     #          return t[i]
     #   return t[-1]            