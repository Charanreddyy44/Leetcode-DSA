class Solution:
    def maxScore(self, s: str) -> int:
        maxScore = 0
        
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            countL = collections.Counter(left)
            countR = collections.Counter(right)
            score = countL['0'] + countR['1']
            maxScore = max(maxScore, score)

        return maxScore