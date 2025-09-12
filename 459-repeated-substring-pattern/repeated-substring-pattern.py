class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
      #  conc = (s+s)[1:-1]
       # return s in conc
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:  # i must divide n
                if s[:i] * (n // i) == s:
                    return True
        return False