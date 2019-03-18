"""
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        _len = len(nums)
        for i in range(_len - 1, -1, -1):
            if nums[i] == 0:
                zero = nums.pop(i)
                nums.append(zero)

    def moveZeroes2(self, nums: list[int]) -> None:
        zeroIndex = 0
        for curr in range(len(nums)):
            if nums[curr] != 0:
                nums[curr], nums[zeroIndex],  = nums[zeroIndex], nums[curr]
                zeroIndex += 1