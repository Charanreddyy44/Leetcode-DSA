class Solution:
    def reformat(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        digits = [c for c in s if c.isdigit()]
        if abs(len(letters) - len(digits)) > 1:
            return ""
        if len(letters) > len(digits):
            first, second = letters, digits
        else:

            first, second = digits, letters
        res = []
        for i in range(len(s)):
            if i % 2 == 0:
                res.append(first[i // 2])
            else:
                res.append(second[i // 2])

        return ''.join(res)    