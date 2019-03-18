"""
The algorithm should run in linear time and in O(1) space.
"""


class Solution:

    def majorityElement(self, nums: list[int]) -> list[int]:
        """
        Boyer-Moore Majority Vote Algorithm:
            由于最多有两个可能的元素，所以我们使用两个 candidate，每个 candidate 对应一个 counter。
        :param nums:
        :return:
        """
