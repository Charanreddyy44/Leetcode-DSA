class Solution(object):
    def maxProduct(self, words):
        n = len(words)
        result = 0
        charsets = [set(w) for w in words]
        for i in range(n):
            for j in range(i + 1, n):
                if charsets[i].isdisjoint(charsets[j]):
                    result = max(result, len(words[i]) * len(words[j]))

        return result      