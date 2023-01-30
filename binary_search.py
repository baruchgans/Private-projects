from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

        # if len(nums) == 0:
        #     return -1
        # mid = len(nums) // 2
        # if target == nums[mid]:
        #     return mid
        # if target < nums[mid]:
        #     return self.search(nums[0:mid], target)
        # return self.search(nums[mid + 1:], target)


#
nums = [-1, 0, 3, 5, 9, 12]
target = 9
# nums = [-1, 0, 3, 5, 9, 12]
# target = 2
sol = Solution()
print(sol.search(nums, target))
