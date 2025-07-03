class Solution(object):
    def minSteps(self, s, t):
        cnt = Counter(s)
        for c in t:
            cnt[c] -= 1

        return sum(abs(v) for v in cnt.values())           
            
            
            
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        