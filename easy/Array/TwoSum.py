class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        re = {}
        for index, value in enumerate(nums):
            val = target-value
            if val in re:
                return [re[val], index]
            else:
                re[value] = index

    def twoSum2(self, nums, targets):
        """
        第二种方案
        :param nums:
        :param targets:
        :return:
        """
        re = {}
        for index, value in enumerate(nums):
            if targets - value in re:
                return [re[targets-value], index]
            re[value] = index

