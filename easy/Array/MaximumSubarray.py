"""
Given an integer array nums, find the contiguous subarray
    (containing at least one number) which has the largest sum and return its sum.
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # time exceeded
        import math
        max = math.inf
        _len = len(nums)
        for index in range(0, _len):  # 1个元素之和,  2个元素之和, ...
            count = 0
            sum = 0
            while index+count < _len:
                sum += nums[index+count]
                if sum > max:
                    max = sum
        return max

    # dynamic programming
    def maxSubArray2(self, nums: list[int]) -> int:
        """
         用dp[i]表示最大子数组的结束下标为i的情形，则对于i-1，有: dp[i]=max{dp[i−1]+nums[i],nums[i]}.
        :param nums:
        :return:
        """
        if not nums:
            return None
        _len = len(nums)
        dp = [0]*_len
        dp[0] = nums[0]     # 初始化
        for i in range(1, _len):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)

    # kadane
    def maxSubArray3(self, nums: list[int]) -> int:
        """
        Kadane算法的简单想法就是寻找所有连续的正的子数组（max_ending_here就是用来干这事的），
        同时，记录所有这些连续的正的子数组中的和最大值。
        每一次我们得到一个数，就将它与max_so_far比较，如果它的值比max_so_far大，则更新max_so_far的值。
        :param nums:
        :return:
        """
        max_so_far = float('-inf')
        max_ending_here = 0
        for index in range(len(nums)):
            max_ending_here += nums[index]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far

    # find max crossing subarray in linear time
    def find_max_crossing_subarray(self, A, low, mid, high):
        max_left, max_right = -1, -1
        # left part of the subarray
        left_sum = float("-Inf")
        sum = 0
        for i in range(mid, low - 1, -1):
            sum += A[i]
            if sum > left_sum:
                left_sum = sum
                max_left = i
        # right part of the subarray
        right_sum = float("-Inf")
        sum = 0
        for j in range(mid + 1, high + 1):
            sum += A[j]
            if sum > right_sum:
                right_sum = sum
                max_right = j
        return max_left, max_right, left_sum + right_sum

    # using divide and conquer to solve maximum subarray problem
    # time complexity: n*logn
    def find_maximum_subarray(self, A, low, high):
        import math
        if high == low:
            return low, high, A[low]
        else:
            mid = math.floor((low + high) / 2)
            left_low, left_high, left_sum = self.find_maximum_subarray(A, low, mid)
            right_low, right_high, right_sum = self.find_maximum_subarray(A, mid + 1, high)
            cross_low, cross_high, cross_sum = self.find_max_crossing_subarray(A, low, mid, high)
            if left_sum >= right_sum and left_sum >= cross_sum:
                return left_low, left_high, left_sum
            elif right_sum >= left_sum and right_sum >= cross_sum:
                return right_low, right_high, right_sum
            else:
                return cross_low, cross_high, cross_sum