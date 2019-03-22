class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        """
        1<=nums[index]<=len(nums)
        对于每个数字nums[i]，如果其对应的nums[nums[i] - 1]是正数，我们就赋值为其相反数(标记信息)，如果已经是负数，就不变了
        那么最后我们只要把留下的整数对应的位置加入结果res中即可，参见代码如下：
        :param nums:
        :return:
        """
        res = []
        for element in nums:
            element = abs(element)
            if nums[element-1] > 0:
                nums[element-1] = -nums[element-1]
        for index in range(len(nums)):
            if nums[index] > 0:
                res.append(index+1)
        return res

    def findDisappearedNumbers2(self, nums: list[int]) -> list[int]:
        """
        Time Limit Exceeded
        第二种方法是将nums[i]置换到其对应的位置nums[nums[i]-1]上去.
        最后在对应位置检验，如果nums[i]和i+1不等，那么我们将i+1存入结果res中即可
        :param nums:
        :return:
        """
        res = []
        nums_len = len(nums)
        index = 0
        while index < nums_len:
            if nums[index] != nums[nums[index]-1] :
                nums[index], nums[nums[index] - 1] = nums[nums[index] - 1], nums[index]
            else:
                index += 1
        for index in range(nums_len):
            if nums[index] != index + 1:
                res.append(index + 1)
        return res

    def findDisappearedNumbers3(self, nums: list[int]) -> list[int]:
        """
        在nums[nums[i]-1]位置累加数组长度n，注意nums[i]-1有可能越界，
        所以我们需要对n取余，最后要找出缺失的数只需要看nums[i]的值是否小于等于n即可
        :param nums:
        :return:
        """

        res = []
        nums_len = len(nums)
        for element in nums:
            nums[(element-1) % nums_len] += nums_len
        for index in range(nums_len):
            if nums[index] <= nums_len:
                res.append(index+1)
        return res

    def findDisappearedNumbers4(self, nums: 'List[int]') -> 'List[int]':
        s = set(nums)
        n = len(nums)
        return [x for x in range(1, n + 1) if x not in s]