#import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[-k]
       # heap = []
       # for num in nums:
       #     heapq.heappush(heap, num)
       #     if len(heap) > k:
       #         heapq.heappop(heap)
       # return heap[0]                