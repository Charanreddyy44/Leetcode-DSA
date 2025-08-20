class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        collected = set()
        ops = 0

        for num in reversed(nums):
            ops += 1
            if 1 <= num <= k:
                collected.add(num)
            if len(collected) == k:
                break

        return ops