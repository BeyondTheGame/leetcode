"""
Given an integer array, you need to find one continuous subarray that
if you only sort this subarray in ascending order, then the whole array
will be sorted in ascending order, too.

给了一个int array，找出一个最短的无序连续子数组，当把这个子数组排序之后，整个array就已经是排序的了。
让我们找出数组中的无序的部分
"""


class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        """
        Time Limit Exceeded
        :param nums:
        :return:
        """
        start = -1  # unsorted array 的起始位置
        len_nums = len(nums)
        res = 0
        for index in range(1, len_nums):
            if nums[index] < nums[index-1]:  # 遇到unsorted额度的情况
                moveElement = nums[index]
                moveIndex = index-1
                while moveIndex >= 0 and nums[moveIndex] > moveElement:
                    moveIndex -= 1
                nums.pop(index)     # 找到插入位置，交换值
                nums.insert(moveIndex+1, moveElement)
                if start == -1 or start > moveIndex+1:
                    start = moveIndex + 1
                res = index - start + 1
        return res

    def findUnsortedSubarray2(self, nums: list[int]) -> int:
        start = -1
        end = -2
        nums_len = len(nums)
        _max = nums[0]
        _min = nums[nums_len - 1]
        for index in range(1, nums_len):
            _max = max(_max, nums[index])
            _min = min(_min, nums[nums_len-1-index])
            if _max > nums[index]:
                end = index
            if _min < nums[nums_len-1-index]:
                start = nums_len-1-index
        return end - start + 1





