class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        slist = list(s)
        slist.reverse()
        res = dic[slist[0]]
        for index in range(1,len(slist)):
            if dic[slist[index]] < dic[slist[index-1]]:
                res += dic[slist[index]]
            else:
                res -= dic[slist[index]]
        return res

    def romanToInt2(self, s):
        """
        :param s: str
        :return: int
        """
        sum = 0
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(s) - 1):
            if roman[s[i]] >= roman[s[i + 1]]:
                sum += roman[s[i]]
            else:
                sum -= roman[s[i]]
        return sum + roman[s[-1]]
