class Solution(object):
    def oddString(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def diff(word):
            return [ord(word[i+1]) - ord(word[i]) for i in range(len(word)-1)]

        diffs = [diff(w) for w in words]
    
    
        for d in diffs:
            if diffs.count(d) == 1:
                return words[diffs.index(d)] 