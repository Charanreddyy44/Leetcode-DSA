class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        XOR_Value = start^goal
        count = 0
        while XOR_Value:
            if XOR_Value & 1 == 1:
                count+=1
            XOR_Value >>= 1    
        return count      
        