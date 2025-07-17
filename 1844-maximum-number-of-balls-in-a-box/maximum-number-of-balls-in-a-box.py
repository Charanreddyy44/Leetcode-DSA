class Solution:
    def countBalls(self, lowLimit, highLimit):
        from collections import defaultdict

        def digit_sum(n):
            return sum(int(d) for d in str(n))

        box_counts = defaultdict(int)

        for i in range(lowLimit, highLimit + 1):
            box = digit_sum(i)
            box_counts[box] += 1

        return max(box_counts.values())
