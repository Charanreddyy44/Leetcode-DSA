class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res = ""
        while columnNumber:
            columnNumber -= 1
            res = chr(65+columnNumber % 26)+res
            columnNumber//= 26
        return res
