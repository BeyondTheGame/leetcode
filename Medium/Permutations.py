class Solution(object):
    def permute(self, nums):
        """
        生成全排列问题
        DFS + visited
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.backtracking(nums, len(nums), [])
        return self.res

    def backtracking(self, nums, nums_len, out: list):
        if len(out) == nums_len:
            self.res.append(out[:])    # 已将全部数选出，满足条件加入结果集，结束递归
        else:
            for index in range(nums_len):
                if nums[index] in out:
                    continue
                out.append(nums[index])
                self.backtracking(nums, nums_len, out)
                out.pop()   # 回溯

    def permute2(self, nums):
        """
        用到一个visited数组来标记某个数字是否访问过.然后在DFS递归函数从的循环应从头开始，而不是从start开始
        :param nums:
        :return:
        """
        self.res = []
        self.backtracking(nums, len(nums), [0]*len(nums), [])
        return self.res

    def backtracking2(self, nums, nums_len, visited, out: list):
        if len(out) == nums_len:
            self.res.append(out)
            return
        else:
            for index in range(nums_len):
                if visited[index] == 1:
                    continue
                visited[index] = 1
                out.append(nums[index])
                self.backtracking2(nums, nums_len, visited, out)
                out.pop()
                visited[index] = 0

    def permute3(self, nums):
        """
        当n=1时，数组中只有一个数a1，其全排列只有一种，即为a1
        当n=2时，数组中此时有a1a2，其全排列有两种，a1a2和a2a1，那么此时我们考虑和上面那种情况的关系，
                我们发现，其实就是在a1的前后两个位置分别加入了a2
        当n=3时，数组中有a1a2a3，此时全排列有六种，分别为a1a2a3, a1a3a2, a2a1a3, a2a3a1, a3a1a2, 和 a3a2a1。
                那么根据上面的结论，实际上是在a1a2和a2a1的基础上在不同的位置上加入a3而得到的。
        _ a1 _ a2 _ : a3a1a2, a1a3a2, a1a2a3
        _ a2 _ a1 _ : a3a2a1, a2a3a1, a2a1a3
        :param nums:
        :return:
        """
        res = [[]]
        for num in nums:
            new_res = []
            for out in res:
                for pos in range(len(out)+1):   # insert position
                    new_res.append(out[:pos]+[num]+out[pos:])
            res = new_res
        return res

    def permute4(self, nums):
        if not nums:
            return [[]]
        return [tmp[:i] + [nums[0]] + tmp[i:] for tmp in self.permute(nums[1:]) for i in range(len(tmp) + 1)]

    def permute5(self, nums):
        self.res = []
        self.swap(nums, 0)
        return self.res

    def swap(self, nums, level):
        if level >= len(nums):
            self.res.append(nums[:])
        for i in range(level, len(nums)):
            nums[level], nums[i] = nums[i], nums[level]
            self.swap(nums, level+1)
            nums[level], nums[i] = nums[i], nums[level]



nums = [2, 3, 5]
sol = Solution()
res = sol.permute5(nums)
print(res)