"""

"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        要找到一对最低价和最高价，最低价在最高价前面，以最低价买入股票，以最低价卖出股票。
        去找到在前一段区间内最小的数，和后一段区间内最大的数，二者之差即为最大收益。
        :param prices:
        :return:
        """
        nums_len = len(prices)
        if nums_len <= 1:
            return 0
        _min = prices[0]     # min是当前时刻的最小值，最大收益值则是不断用当前值减去最小值，不断的更新min值以及最大收益值。
        index = 1
        res_income = 0  # 返回的收入
        while index < nums_len:
            income = prices[index] - _min
            res_income = max(res_income, income)
            _min = min(_min, prices[index])
            index += 1
        return res_income
