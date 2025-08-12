class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        next = {}
        for num in nums2:
            while stack and num > stack[-1]:
                next[stack.pop()] = num
            stack.append(num)
        for num in stack:
            next[num] = -1
        return [next[x] for x in nums1]        