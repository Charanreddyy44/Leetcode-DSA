class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        for i in range(n):
            for j in reversed (result):
                result.append(j|(1<<i))
        return result        

