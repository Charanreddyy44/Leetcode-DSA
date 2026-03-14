class Solution(object):
    def minimumIndex(self, capacity, itemSize):
        """
        :type capacity: List[int]
        :type itemSize: int
        :rtype: int
        """
        res = []
        for i in range(len(capacity)):
            if capacity[i] >= itemSize:
                res.append(capacity[i])
        if len(res) == 0:
            return -1
        s = min(res)
        for i in range(len(capacity)):
            if capacity[i] == s:
                return i



