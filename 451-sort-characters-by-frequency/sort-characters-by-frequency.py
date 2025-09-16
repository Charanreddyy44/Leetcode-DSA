from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)
        sorted_s = sorted(freq, key = lambda c: -freq[c])
        result = ""
        for ch in sorted_s:
            result += ch*freq[ch]
        return result    