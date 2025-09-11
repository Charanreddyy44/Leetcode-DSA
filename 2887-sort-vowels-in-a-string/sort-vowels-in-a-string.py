class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vs = [c for c in s if c.lower() in "aeiou"]
        vs.sort()
        cs = list(s)
        j = 0
        for i, c in enumerate(cs):
            if c.lower() in "aeiou":
                cs[i] = vs[j]
                j += 1
        return "".join(cs)
