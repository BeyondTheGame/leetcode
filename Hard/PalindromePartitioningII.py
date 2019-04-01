class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        strlen = len(s)
        # dp[i]表示子串 [0, i] 范围内的最小分割数
        # return dp[n-1]
        dp = [] * strlen
        """
        更新dp[]
        [0, i] 这个区间的每个位置都可以尝试分割开来，用一个变量j来从0遍历到i，这样就可以把区间 [0, i] 分为两部分:
        [0, j-1] 和 [j, i]。 
        我们是从前往后更新的，而 j 小于等于 i，所以 dp[j-1] 肯定在 dp[i] 之前就已经算出来了。
        这样就只需要判断区间 [j, i] 内的子串是否为回文串了，是的话，dp[i] 就可以用 1 + dp[j-1] 来更新了。
        p[i][j] 表示区间 [i, j] 内的子串是否为回文串。 
        """
        P = [[False for i in range(strlen)] for i in range(strlen)]
        for i in range(strlen):
            dp[i] = i
            for j in range(i+1):
                if s[i] == s[j] and(i-j <= 1 or P[j+1][i-1]):
                    P[j][i] = True
                    dp[i] = 0 if j == 0 else min(dp[i], dp[j-1]+1)
        return dp[strlen-1]

    def minCut2(self, s):
        """
        dp[i] 表示由s串中前 i 个字母组成的子串的最小分割数，这样 dp[n] 极为最终所求。
        道题更新的是 dp[i+len+1] 和 dp[i+len+2]，其中 len 是以i为中心，总长度为 2*len + 1 的回文串
        :param s:
        :return:
        """
        import sys
        if not s:
            return 0
        strlen = len(s)
        # dp[i] 是区间[0, i-1] 的最小分割数
        dp = [sys.maxsize] * (strlen+1)
        dp[0] = -1
        for i in range(strlen):
            _len = 0
            while i - _len >= 0 and i + _len < strlen and s[i-_len] == s[i+_len]:
                dp[i+_len+1] = min(dp[i+_len+1], 1 + dp[i - _len])
                _len += 1
            _len = 0
            while i - _len >= 0 and i+_len+1 < strlen and s[i-_len] == s[i+_len+1]:
                dp[i+_len+2] = min(dp[i+_len+2], 1+dp[i-_len])
                _len += 1
        return dp[strlen]