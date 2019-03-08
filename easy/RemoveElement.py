class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            if nums[start] == val:
                nums.pop(start)
                end -= 1
            else:
                start += 1
        return start

    def removeElement2(self, nums: list[int], val: int) -> int:
        for index in range(len(nums)-1, -1, -1):
            if nums[index] == val:
                nums.pop(index)
        return len(nums)

    def removeElement3(self, nums: list[int], val: int) -> int:
        length = len(nums)
        if length == 0:
            return 0
        right = length-1
        for index in (right, -1, -1):
            if nums[index] == val:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1
        return max(right+1, 0)