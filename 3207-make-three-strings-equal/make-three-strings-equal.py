class Solution(object):
    def findMinimumOperations(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: int
        """
        min_len = min(len(s1), len(s2), len(s3))
        i = 0

    # Find the length of the common prefix
        while i < min_len and s1[i] == s2[i] and s2[i] == s3[i]:
            i += 1

    # If no common prefix at all, it's impossible
        if i == 0:
            return -1

    # We need to delete the remaining characters after the common prefix
        return (len(s1) - i) + (len(s2) - i) + (len(s3) - i)