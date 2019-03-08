class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for index in range(len(nums) - 1, 0, -1):
            if nums[index] == nums[index - 1]:
                nums.pop(index)
        return len(nums)

    def removeDuplicates2(self, nums: list[int]) -> int:
        if not nums:
            return 0
        newTail = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]
        return newTail + 1
