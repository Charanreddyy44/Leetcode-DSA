class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        rep_num = digit
        count = 0
        for num in nums:
            if num == 0 and rep_num == 0:
                count += 1
            while num > 0:
                if num % 10 == rep_num:
                    count += 1
                num //= 10
        return count