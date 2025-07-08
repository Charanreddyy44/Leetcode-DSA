class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = "aeiouAEIOU"
        count1 = 0
        count2 = 0
        n = len(s)
        for i in range(n//2):
            if s[i] in vowels:
                count1 += 1
        for i in range(n//2, n):
            if s[i] in vowels:
                count2 += 1
        return count1 == count2
            