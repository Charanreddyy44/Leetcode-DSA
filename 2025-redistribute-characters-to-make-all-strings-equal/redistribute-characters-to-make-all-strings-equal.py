from collections import Counter

class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        total_count = Counter()
        for word in words:
            total_count.update(word)
    
        n = len(words)
    
        for char in total_count:
            if total_count[char] % n != 0:
                return False
    
        return True
        
        
