class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        nums = sorted(nums)
        self.helper(nums, [0]*len(nums), len(nums), [])
        return self.res

    def helper(self, nums, visited, nums_len, out):
        if len(out) == nums_len:
            self.res.append(out[:])
            return
        else:
            for index in range(nums_len):
                if visited[index] == 1 or index > 0 and nums[index-1] == nums[index] \
                        and visited[index-1] == 0:
                    continue
                visited[index] = 1
                out.append(nums[index])
                self.helper(nums, visited, nums_len, out)
                visited[index] = 0
                out.pop()


nums = [1, 2, 2]
sol = Solution()
res = sol.permuteUnique(nums)
print(res)