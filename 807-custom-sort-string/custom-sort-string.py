from collections import Counter
class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """

        count = Counter(s)
        result = []
        for char in order:
            if char in count:
                result.append(char * count[char])
                del count[char] 
        for char in count:
            result.append(char * count[char])

        return ''.join(result)