class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = {}
        for element in nums:
            if element in count.keys():
                count[element] += 1
            else:
                count[element] = 1
        # return max(count, key=count.get)
        max = 0
        maxIndex = -1
        for key, val in count.items():
            if val > max:
                max = val
                maxIndex = key
        return maxIndex

    def majorityElement(self, nums: list[int]) -> int:
        """
        摩尔投票法 Moore Voting
        这种投票法先将第一个数字假设为众数，然后把计数器设为1，比较下一个数和此数是否相等，若相等则计数器加一，反之减一。
        然后看此时计数器的值，若为零，则将下一个值设为候选众数。以此类推直到遍历完整个数组，当前候选众数即为该数组的众数。
        前提: 一定会有一个出现超过半数的数字存在，

        如果计数器减到0了话，说明到目前位置， 不是候选者数字的个数已经跟候选者的出现个数相同了，
        余下部分的多数元素依然是原数组的多数元素。
        :param nums:
        :return:
        """
        res = 0
        count = 0
        for element in nums:
            if count == 0:
                res = element
                count += 1
            elif element == res:
                count += 1
            else:
                count -= 1
        return res