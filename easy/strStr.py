class Solution:
    """
    字符串中寻找子串
    """
    def strStr(self, haystack: str, needle: str) -> int:
        """
        What should we return when needle is an empty string?
        This is a great question to ask during an interview.
        For the purpose of this problem, we will return 0 when needle is an empty string.
        This is consistent to C's strstr() and Java's indexOf().
        """
        if haystack is None:
            return -1
        elif needle is None:
            return 0
        try:
            index = haystack.index(needle)
            return index
        except:
            return -1

    def brute_strStr(self, haystack: str, needle: str) -> int:
        """
        暴力破解
        """
        if needle is None or haystack is None:
            return
        tlen = len(haystack)
        plen = len(needle)  # p 模式
        if plen == 0:
            return 0
        elif tlen == 0:
            return -1
        tindex, pindex = 0, 0
        for tindex in range(tlen-plen+1):
            for pindex in range(plen):
                if needle[pindex] == haystack[pindex+tindex]:
                    pindex += 1
                else:
                    break
            if pindex == plen:   # matched
                return tindex
            else:
                pindex = 0
                tindex += 1
        else:
            return -1

    def fail(self, pattern, string):
        """
        求pattern每个位置的回溯位置
        :param pattern:
        :param string:
        :return:
        """
        plen = len(pattern)
        f = [-1]  # 初始化非f[] 第一个位置为-1
        # for j in range(1, plen):

