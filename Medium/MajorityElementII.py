"""
The algorithm should run in linear time and in O(1) space.
"""


class Solution:

    def majorityElement(self, nums: list[int]) -> list[int]:
        """
        Boyer-Moore Majority Vote Algorithm:
            由于最多有两个可能的元素，所以我们使用两个 candidate，每个 candidate 对应一个 counter。
        先判断当前元素是否与 candidate 相匹配，若不匹配，则判断是否要更新 candidate，若也不需要更新，
        则已经获取了三个不同的元素，即当前元素和两个 candidate，去除的方式是两个 counter 同时减一。
        不能类似 Majority Element 那样，使用数组的前两个元素作为两个 candidate，因为数组的前两个元素可能是相同的。
        其实解决办法也很简单，只要给两个 candidate 赋予不同的初值，并且两个 counter 的初值均为 0 即可。
        如果先判断 counter，则有可能出现两个 candidate 相同的情况
        :param nums:
        :return:
        """
        def validate(nums: list[int], candidate):
            """
            判断candidate元素的个数是否大于len(nums)的1/3
            :param nums:
            :param candidate:
            :return:
            """
            count = 0
            for ele in nums:
                if ele == candidate:
                    count += 1
            if count > len(nums) // 3:
                return True
            else:
                return False
        res = []
        candidate_1, candidate_2 = 0, 1
        count_1, count_2 = 0, 0
        for element in nums:
            if element == candidate_1:
                count_1 += 1
            elif element == candidate_2:
                count_2 += 1
            elif count_1 == 0:
                candidate_1 = element
                count_1 = 1
            elif count_2 == 0:
                candidate_2 = element
                count_2 = 1
            else:
                count_1 -= 1
                count_2 -= 1
        if validate(nums, candidate_1):
            res.append(candidate_1)
        if validate(nums, candidate_2):
            res.append(candidate_2)
        return res