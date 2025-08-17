class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(str, nums))
        def compare(a, b):
            if a+b > b+a:
                return -1
            elif a+b < b+a:
                return 1
            else:
                return 0
                                      # Sort using custom comparator
        nums.sort(key=cmp_to_key(compare))
    
                                      # Join the sorted numbers
        result = ''.join(nums)
    
                                # Handle case like [0,0] → "0" (not "00")
        return '0' if result[0] == '0' else result            