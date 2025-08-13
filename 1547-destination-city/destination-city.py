class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        starts = {start for start,_ in paths}
        for _, end in paths:
            if end not in starts:
                return end
        