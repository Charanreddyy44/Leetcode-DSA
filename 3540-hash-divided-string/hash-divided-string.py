class Solution(object):
    def stringHash(self, s, k):

        result = ""
        for i in range(0, len(s),k):
            substring = s[i:i+k]
            total = 0
            for char in substring:
                total += ord(char) - ord('a')
            hashed_char = chr((total % 26) + ord('a'))
            result += hashed_char
        return result
        