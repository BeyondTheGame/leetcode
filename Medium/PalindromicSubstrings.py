class Solution(object):
    def countSubstrings(self, s):
        """
        以字符串中的每一个字符都当作回文串中间的位置，然后向两边扩散，每当成功匹配两个左右两个字符，
        结果res自增1，然后再比较下一对。
        注意回文字符串有奇数和偶数两种形式，如果是奇数长度，那么i位置就是中间那个字符的位置，
        所以我们左右两遍都从i开始遍历；如果是偶数长度的，那么i是最中间两个字符的左边那个，右边那个就是i+1。
        :type s: str
        :rtype: int
        """
        self.res = 0
        for index in range(0, len(s)):
            self.helper(s, index, index)    # 奇数
            self.helper(s, index, index + 1)    # 偶数长度
        return self.res

    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            self.res += 1

    def countSubstrings2(self, s):
        """
        dp[i][j] = True if s[i:j+1] is palidrome string
        or dp[i][j] = the numbers of palidrome substring of s[i:j+1] , return dp[0][n-1]
        :param s:
        :return:
        """
        res = 0
        strlen = len(s)
        dp = [[False for i in range(strlen)] for i in range(strlen)]
        for i in range(strlen-1, -1, -1):
            for j in range(i, strlen):
                dp[i][j] = (s[i] == s[j]) and (j-i <= 1 or dp[i+1][j-1])
                if dp[i][j]:
                    res += 1
        return res

    def countSubstrings3(self, s):
        res = 0
        strlen = len(s)
        dp = [[False for i in range(strlen)] for i in range(strlen)]
        endIndex = 0
        while endIndex < strlen:
            startIndex = 0
            while startIndex <= endIndex:
                if s[startIndex] == s[endIndex] and (endIndex - startIndex <= 1 or dp[startIndex+1][endIndex-1]):
                    dp[startIndex][endIndex] = True
                    res += 1
                startIndex += 1
            endIndex += 1
        return res


s = 'aab'
sol = Solution()
res = sol.countSubstrings3(s)
print(res)

