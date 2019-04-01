class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(nums, [], 0)
        return self.res

    def helper(self, nums, out, start):
        if len(out) <= len(nums):
            self.res.append(out[:])
        for index in range(start, len(nums)):
            out.append(nums[index])
            self.helper(nums, out, index+1)
            out.pop()


nums = [1, 2, 3]
sol = Solution()
res = sol.subsets(nums)
print(res)