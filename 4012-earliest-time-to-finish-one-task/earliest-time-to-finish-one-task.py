class Solution(object):
    def earliestTime(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        result = [sum(inner)for inner in tasks]
        return min(result)