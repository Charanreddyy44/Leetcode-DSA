class Solution(object):
    def largestEven(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_two = s.rfind('2')
        if last_two == -1:
            return ""
        return s[:last_two + 1]