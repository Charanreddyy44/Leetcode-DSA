class Solution(object):
    def count_ones(self, n):
        count = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            n = n // 2
        return count
    def sort_key(self, x):
        return (self.count_ones(x), x)

    def sortByBits(self, arr):
        arr.sort(key=self.sort_key)
        return arr
        
        


            