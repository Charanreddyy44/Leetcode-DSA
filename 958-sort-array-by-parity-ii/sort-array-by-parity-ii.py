class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        e = o = 0
        even = [x for x in nums if x%2 == 0]
        odd = [x for x in nums if x%2 != 0]
        for i in range(len(nums)):
            if i%2 == 0:
                res.append(even[e])
                e+=1
            else:    
                res.append(odd[o])
                o+=1
        return res