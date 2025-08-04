class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trusted_by = [0] * (n + 1)
        trusts = [0] * (n + 1)

        for a, b in trust:
            trusts[a] += 1      # a trusts someone
            trusted_by[b] += 1  # b is trusted by a

        for person in range(1, n + 1):
            if trusts[person] == 0 and trusted_by[person] == n - 1:
                return person

        return -1