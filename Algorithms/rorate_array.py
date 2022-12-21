class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            move = nums.pop()
            nums.insert(0, move)
        return nums


nums = [1,2,3,4,5,6,7]
k = 3
print(Solution().rotate(nums,k))