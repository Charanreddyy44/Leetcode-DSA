class Solution(object):
    def fairCandySwap(self, A, b):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        difference = (sum(A)-sum(b))//2;
        A = set(A)
        for i in set(b):
            if i+difference in A:
                return [difference + i,i]