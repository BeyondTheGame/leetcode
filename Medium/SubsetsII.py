class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        nums = sorted(nums)
        self.backtracking(nums, [], 0)
        return self.res

    def backtracking(self, nums, out, start):
        self.res.append(out[:])
        for index in range(start, len(nums)):
            if index > start and nums[index] == nums[index-1]:
                continue
            out.append(nums[index])
            self.backtracking(nums, out, index+1)
            out.pop()

