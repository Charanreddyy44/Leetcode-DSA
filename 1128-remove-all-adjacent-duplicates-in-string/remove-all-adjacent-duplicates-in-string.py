class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for char in s:
            if result and result[-1] == char:
                result = result[:-1]
            else:
                result += char
        return result    