class Solution(object):
    def mostCommonWord(self, pgh, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        pgh = pgh.lower()
        for ch in "!?',;.":
            pgh = pgh.replace(ch, " ")
        words = pgh.split()
        banned_set = set(banned)
        freq = {}
        for word in words:
            if word not in banned_set:
                freq[word] = freq.get(word,0)+1
        return max(freq, key = freq.get)