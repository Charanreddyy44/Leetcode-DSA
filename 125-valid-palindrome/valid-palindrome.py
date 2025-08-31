class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        rev = ' '.join(ch.lower() for ch in s if ch.isalnum())
        return  rev == rev[::-1]