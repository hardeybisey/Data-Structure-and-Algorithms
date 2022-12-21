class Solution(object):
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = {}
        for index, num in enumerate(nums):
            check = target - num

            if check in mapping:
                return [mapping[check], index]
            mapping[num] = index


nums = [3, 2, 4]
target = 6
ans = Solution()
print(ans.two_sum(nums, target))
