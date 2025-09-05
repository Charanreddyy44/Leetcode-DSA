class Solution(object):
    def minPartitions(self, c):
        
        max_digit = 0
        for ch in c:
            b = ord(ch) - ord('0')
            max_digit = max_digit ^ ((max_digit^b)&- (max_digit < b))
        return max_digit    