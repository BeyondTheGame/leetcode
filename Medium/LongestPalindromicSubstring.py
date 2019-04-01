class Solution(object):
    def longestPalindrome(self, s):
        """

        Brute Force: 以每一个字符为中心，像两边扩散来寻找回文串
        :type s: str
        :rtype: str
        """
        self.maxlen = 0
        self.maxStart = 0
        strlen = len(s)
        if strlen <= 1:
            return s
        for index in range(0, strlen):
            self.searchPalindrome(s, strlen, index, index)
            self.searchPalindrome(s, strlen, index, index + 1)
        return s[self.maxStart:self.maxStart + self.maxlen]

    def searchPalindrome(self, s, strlen, left, right):
        while left >= 0 and right < strlen and s[left] == s[right]:
            left -= 1
            right += 1
        if right - left - 1 > self.maxlen:
            self.maxlen = right - left - 1
            self.maxStart = left + 1

    def longestPalindrome2(self, s):
        """
        brute force
        :param s:
        :return:
        """
        strlen = len(s)
        if strlen <= 1:
            return s
        maxlen = 0
        start = 0
        index = 0
        while index < strlen:
            # 剩余的字符数是否小于等于maxLen的一半，是的话说明maxLen无法再变长了，直接break掉.
            if (strlen - index) <= maxlen / 2:
                break
            left = right = index
            # 先要做的是向右遍历跳过重复项
            while right < strlen - 1 and s[right + 1] == s[right]:
                right += 1
            index = right + 1
            while right < strlen - \
                    1 and left > 0 and s[right + 1] == s[left - 1]:
                right += 1
                left -= 1
            if maxlen < right - left + 1:
                maxlen = right - left + 1
                start = left
        return s[start: start + maxlen]

    def longestPalindrome3(self, s):
        strlen = len(s)
        if strlen <= 1:
            return s
        # dp[i][j] = True  如果字符串区间[i, j]为回文串
        maxlen = 1
        start = 0
        dp = [[False for i in range(strlen)] for i in range(strlen)]
        for end in range(0, strlen):
            dp[end][end] = True
            for i in range(0, end):
                dp[i][end] = (s[i] == s[end] and (end - i <= 1 or dp[i + 1][end - 1]))
                if dp[i][end] and maxlen < end - i + 1:
                    maxlen = end - i + 1
                    start = i
        return s[start:start + maxlen]

    def longestPalindrome_manacher(self, s):
        string = '$#'
        for index in range(len(s)):     # 预处理
            string += s[index]
            string += '#'
        string += '@'
        strlen = len(string)
        dp = [0] * strlen   # dp[i] 表示string中以i为中心的回文子串的半径
        mxId = mx = resId = resRadii = 0
        for i in range(1, strlen - 1):
            j = 2*mxId-i      # j =2*id - i 是i关于id的对称
            dp[i] = min(dp[j], mx-i) if mx > i else 1
            while string[i+dp[i]] == string[i-dp[i]]:
                dp[i] += 1
            if i+dp[i] > mx:    # 更新mx, id
                mx = i+dp[i]
                mxId = i
            if dp[i] > resRadii:
                resRadii = dp[i]
                resId = i
        start = (resId - resRadii)//2
        return s[start:start+resRadii-1]

s = 'ac'
sol = Solution()
re = sol.longestPalindrome_manacher(s)
print(re)
