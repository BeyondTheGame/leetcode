class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        res = ''
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

    def longestCommonPrefix2(self, strs):
        """
        先将给的字符串数组排序，然后只需要比较第一个和最后一个的公共前缀即可。
        虽然看起来比前面简单了很多，但实际上排序的代价并不低。
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        strs.sort()
        res = ''
        for i in range(len(strs[0])):
            if i >= len(strs[-1]) or strs[-1][i] != strs[0][i]:
                return res
            res += strs[0][i]
        return res

    def longestCommonPrefix3(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                return strs[0][:i]
        return min(strs)
