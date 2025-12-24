class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        total_apples = sum(apple)
        capacity.sort(reverse=True)
        total_capacity = 0
        boxes_used = 0
        for c in capacity:
            total_capacity += c
            boxes_used += 1
            if total_capacity >= total_apples:
                return boxes_used
        return boxes_used
        