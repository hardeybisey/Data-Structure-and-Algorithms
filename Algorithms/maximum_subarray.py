class Solution(object):
    def max_sub_array(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_sum = 0
        best_sum = 0
        for num in nums:
            new_sum = max(0, new_sum + num)
            best_sum = max(best_sum, new_sum)
        return best_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().max_sub_array(nums))
