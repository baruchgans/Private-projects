from typing import List


class Solution(object):
    def combinationSum(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret

    def dfs(self, nums, target, path, ret):
        if target < 0:
            return
        if target == 0:
            ret.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:], target - nums[i], path + [nums[i]], ret)

sol = Solution()
candidates = [2, 3, 5]
candidates2 = [2, 3, 6, 7]
candidates3 = [3, 4, 7, 8]

target = 8
target2 = 7
target3 = 11
print(sol.combinationSum(candidates, target))
print(sol.combinationSum(candidates2, target2))
print(sol.combinationSum(candidates3, target3))
