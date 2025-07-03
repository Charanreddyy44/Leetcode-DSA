class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ans = 0
        cnt = Counter()
        for s in words:
            x = 0
            for c in map(ord, s):
                x |= 1 << (c - ord("a"))
            ans += cnt[x]
            cnt[x] += 1
        return ans