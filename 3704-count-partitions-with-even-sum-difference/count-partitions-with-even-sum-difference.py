class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) % 2 :
            return 0
        else:
            return len(nums) - 1    


       # total_sum = sum(nums)
       # left_sum = 0
       # count = 0
       # for i in range(len(nums)-1):
       #     left_sum += nums[i]
       #     right_sum = total_sum - left_sum
       #     if (left_sum % 2) == (right_sum % 2):
       #         count += 1
       # return count    