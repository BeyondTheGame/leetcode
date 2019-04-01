"""
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
"""


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, out, res):
        """
        将已经检测好的回文子串放到字符串数组out中，当s遍历完了之后，将out加入结果res中
        :param s:
        :param out:
        :param res:
        :return:
        """
        if not s:  # backtracking
            res.append(out[:])
        for index in range(1, len(s) + 1):
            if self.isPar(s[:index]):
                self.dfs(s[index:], out + [s[:index]], res)   # 递归一次，切分余下的字符串一次

    def isPar(self, s):
        return s == s[::-1]

    def partition2(self, s):
        """

        :param s:
        :return:
        """
        str_len = len(s)
        """
        dp[i][j]= True if substring str[i..j] is palindrome, else false
        这样就不需要另外的子函数去判断子串是否为回文串了，大大的提高了计算的效率.
        """
        dp = [[False for col in range(str_len)] for row in range(str_len)]
        for i in range(str_len):    # i: start index
            for j in range(i, str_len):    # j: end index
                if self.isPar(s[i: j+1]):
                    dp[i][j] = True
        self.res = []
        self.dfs_2(s, 0, [], dp)
        return self.res

    def dfs_2(self, string, start: int, out, dp):
        if start == len(string):
            self.res.append(out[:])
            return
        for index in range(start, len(string)):
            if not dp[start][index]:
                continue
            self.dfs_2(string, index+1, out+[string[start:index+1]], dp)

    def partition3(self, s):
        """
        res[i] 表示前i个字符组成的子串，即范围 [0, i+1] 内的子串的所有拆分方法，那么最终只要返回 res[n] 极为所求
        res : 三维数组
        :param s:
        :return:
        """

        strlen = len(s)
        res = [None] * strlen
        dp = [[False for col in range(strlen)] for row in range(strlen)]
        for i in range(strlen):  # i: end index
            res[i] = []     # 二维数组
            for left in range(i+1):  # left: start index
                if s[left] == s[i] and (i - left <= 1 or dp[left+1][i-1]):
                    dp[left][i] = True
                substr = s[left:i+1]
                # 求 res[n]
                for relist in res[left]:
                    relist.append(substr[:])
                    res[i+1].append(relist[:])
        return res[strlen-1]



s = 'aab'
sol = Solution()
res = sol.partition3(s)
print(res)