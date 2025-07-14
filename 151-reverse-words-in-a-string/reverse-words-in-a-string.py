class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = [word for word in s.split(" ") if word]
        return " ".join(reversed(words))
        