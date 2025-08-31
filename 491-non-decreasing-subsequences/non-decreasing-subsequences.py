class Solution(object):
    def findSubsequences(self, nums):
        n = len(nums)
        ans = set()
        for num in range(1<<n):
            subseq = []
            for i in range(n):
                if num & (1<<i):
                    subseq.append(nums[i])
            if len(subseq) >= 2 and all(subseq[i] <= subseq[i+1] for i in    range(len(subseq)-1)):
                ans.add(tuple(subseq))  

        return [list(x) for x in ans]
            
