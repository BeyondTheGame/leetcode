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

    def Horspool_strStr(self, haystack: str, needle: str):
        """
        :param pattern:
        :param string:
        :return:
        """
        pattern_len = len(needle)
        text_len = len(haystack)
        # 以字母表中可打印字符为索引的数组
        move_tabel = [pattern_len] * 96
        for index in range(0, pattern_len - 1):
            # 模式串中每个字符的移动距离，从左至右扫描模式，相同字符的最后一次改写恰好是该字符在模式串的最右边
            move_tabel[ord(needle[index])-32] = pattern_len-1-index
        pattern_lastIndex = pattern_len-1  # 模式中最后一个字符在文本中的位置
        while pattern_lastIndex < text_len:
            k = 0
            while k < pattern_len and needle[pattern_len-1-k] == haystack[pattern_lastIndex-k]:
                k += 1
            if k == pattern_len:
                return pattern_lastIndex - pattern_len + 1
            else:   # 模式向右移动
                pattern_lastIndex += move_tabel[ord(haystack[pattern_lastIndex])-32]
        return -1

    def BoyerMoore_strStr(self, haystack: str, needle: str):
        pattern_len = len(needle)
        text_len = len(haystack)
        badCharacterMoveTable = [pattern_len] * 96      # 坏符号移动表
        for index in range(0, pattern_len-1):
            badCharacterMoveTable[ord(needle[index])-32] = pattern_len-1-index
        goodsuffixMoveTable = self.suffix(needle, pattern_len)
        pattern_lastIndex = pattern_len -1
        while pattern_lastIndex < text_len:
            k = 0
            while k < pattern_len and needle[pattern_len-1-k] == haystack[pattern_lastIndex-k]:
                k += 1
            if k == pattern_len:
                return pattern_lastIndex - pattern_len +1
            else:
                if k == 0:
                    pattern_lastIndex += badCharacterMoveTable[ord(haystack[pattern_lastIndex])-32]
                else:
                    pattern_lastIndex += max(max(1, badCharacterMoveTable[ord(haystack[pattern_lastIndex])-32]-k),
                                             goodsuffixMoveTable[pattern_len-1-k])
        return -1

    def suffix(self, pattern: str, pattern_len: int):
        """
        计算好后缀移动表
        :param pattern:
        :return:
        """
        """
        Each entry shift[i] contain the distance pattern will shift if mismatch occur at position i-1. 
        That is, the suffix of pattern starting at position i is matched and a mismatch occur at position i-1
        """

        """
        Each entry bpos[i] contains the starting index of border for suffix starting at index i 
        in given pattern P.
        -----------------------------------------------------------------------------------------
        lping:  for suffix starting at index i(substring of pattern) , bpos[i] is the starting  of 
                border in pattern T
        -----------------------------------------------------------------------------------------
        The suffix φ beginning at position m has no border, so bpos[m] is set to m+1 where m 
        is the length of the pattern.
        """
        """
          if border[i] = j then border[i-1] = j-1
        """
        goodsuffix_shift = [0] * (pattern_len+1)
        bPos = [0] * (pattern_len+1)
        i = pattern_len
        j = pattern_len + 1
        bPos[i] = j
        while i > 0:
            while j <= pattern_len and pattern[i-1] != pattern[j-1]:

                if goodsuffix_shift[j] == 0:
                    goodsuffix_shift[j] = j - i
                j = bPos[j]
            i -= 1
            j -= 1
            bPos[i] = j

        # case 2
        j = bPos[0]
        for i in range(pattern_len+1):
            if goodsuffix_shift[i] == 0:
                goodsuffix_shift[i] = j
            if i == j:
                j = bPos[j]
        return goodsuffix_shift

    def KMP_strStr(self, haystack: str, needle: str) -> int:
        """"""
        """
        lps[i] = the longest proper prefix of pattern[0..i] which is also a suffix of pattern[0..i]. 
        A proper prefix is prefix with whole string not allowed. 
        when mismatch:
            j = lps[j-1]
            txt[i] and pat[j] do NOT match and j is 0, we do i++.
        """

        pattern_len = len(needle)
        text_len = len(haystack)
        text_index = 0
        pattern_index = 0
        lps = self.computeLPArray(needle, pattern_len)
        while text_index < text_len:
            if needle[pattern_index] == haystack[text_index]:
                pattern_index += 1
                text_index += 1
            if pattern_index == pattern_len:   # Found
                return text_index-pattern_index
            elif text_index < text_len and needle[pattern_index] != haystack[text_index]:
                if pattern_index != 0:
                    pattern_index = lps[pattern_index-1]
                else:
                    text_index += 1
        return -1

    def computeLPArray(self, pattern, pattern_len):
        lps = [0] * pattern_len     # lps[0] is always 0
        index = 1
        _len = 0  # length of the previous longest prefix suffix
        while index < pattern_len:     # the loop calculates lps[i] for i = 1 to pattern_len
            if pattern[index] == pattern[_len]:
                _len += 1
                lps[index] = _len
                index += 1
            else:
                # This is tricky. Consider the example. AAACAAAA and i = 7. The idea is similar to search step.
                if _len != 0:
                    _len = lps[_len - 1]
                else:
                    lps[index] = 0
                    index += 1
        return lps
