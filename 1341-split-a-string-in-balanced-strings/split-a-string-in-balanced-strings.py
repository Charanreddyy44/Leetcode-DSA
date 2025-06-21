class Solution:
    def balancedStringSplit(self, s: str) -> int:
        rslt = 0
        cnt = 0
        for char in s:
            if char == 'R':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                rslt += 1
        return rslt

