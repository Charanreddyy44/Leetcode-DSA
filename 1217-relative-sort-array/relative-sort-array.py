class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        freq = {}
        for num in arr1:
            freq[num] = freq.get(num, 0) + 1
        result = []
        for num in arr2:
            result.extend([num] * freq[num])
            del freq[num]
        remaning = []
        for num in freq:
            remaning.extend([num] * freq[num])
        result.extend(sorted(remaning))
        return result        