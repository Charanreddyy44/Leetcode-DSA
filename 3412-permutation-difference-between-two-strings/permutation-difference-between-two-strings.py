class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
    
        index_s = {char: idx for idx, char in enumerate(s)}
        index_t = {char: idx for idx, char in enumerate(t)}

        total_diff = 0
        for char in s:
            total_diff += abs(index_s[char] - index_t[char])
    
        return total_diff