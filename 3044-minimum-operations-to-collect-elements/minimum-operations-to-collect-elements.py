class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        collected = set()
        op = 0

        for num in reversed(nums):
            op += 1
            if 1 <= num <= k:
                collected.add(num)
            if len(collected) == k:
                break

        return op