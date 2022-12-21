class Solution(object):
    def first_recurring_char(self, array):
        seen = []
        for nums in array:
            if nums in seen:
                return nums
            else:
                seen.append(nums)
        return 'undefined'


# Given an array = [2,5,1,2,3,5,1,2,4]: return 2
# Given an array = [2,1,1,2,3,5,1,2,4]: return 1
# Given an array = [2,3,4,5]: return undefined
# Given an array = [2,5,5,2,3,5,1,2,4] return 5

array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
solution = Solution()
print(solution.first_recurring_char(array))
