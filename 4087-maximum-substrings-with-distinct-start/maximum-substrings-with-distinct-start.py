class Solution:
    def maxDistinct(self, s: str) -> int:
        new_set = set(s)
        return len(new_set)