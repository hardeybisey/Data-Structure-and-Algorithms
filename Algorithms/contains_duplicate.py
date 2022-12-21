class Solution(object):
    def contains_duplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for num in nums:
            if nums.count(num) > 1:
                return "true"

        return "false"


nums = [1,1,1,3,3,4,3,2,4,2]
print(Solution().contains_duplicate(nums))