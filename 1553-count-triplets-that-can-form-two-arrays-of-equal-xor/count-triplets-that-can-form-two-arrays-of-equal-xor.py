class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        ans = 0
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] ^ arr[i]
        for i in range(n):
            for k in range(i+1, n):
                if prefix[i] == prefix[k+1]:
                    ans += (k-i)
        return ans        