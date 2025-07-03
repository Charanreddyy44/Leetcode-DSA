class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        from collections import Counter
        count = Counter(word)

        for ch in count:
            count[ch] -= 1
            if count[ch] == 0:
                del count[ch]
            freq_set = set(count.values())
            if len(freq_set) == 1:
                return True
            count[ch] = count.get(ch, 0) + 1

        return False