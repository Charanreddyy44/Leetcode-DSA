class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
    
        nversion1 = version1.split(".")
        nversion2 = version2.split(".")
        n = max(len(version1), len(version2))
        for i in range(n):
            a = int(nversion1[i]) if i < len(nversion1) else 0
            b = int(nversion2[i]) if i < len(nversion2) else 0
           
            if a > b:
                return 1
            elif b>a:
                return -1
        return 0         
