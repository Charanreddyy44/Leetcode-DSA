from collections import Counter
class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = "aeiou"
        count = Counter(s)
        vowel = sum(count[ch] for ch in vowels)
        const = sum(count[ch] for ch in count if ch.isalpha() and ch not in vowels)
        if const:
            return vowel//const
        else:
            return 0    

