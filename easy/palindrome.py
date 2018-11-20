class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xlist = tuple(str(x))
        for i in range(len(xlist)//2):
            if xlist[i] != xlist[-1-i]:
                return False
        else:
            return True

    def isPalindrome2(self, x):
        x = str(x)
        return x[::-1] == x

    def isPalindrome3(self, x):
        if x < 0:
            return False
        reverseX = str(x)[::-1]
        if x == int(reverseX):
            return True
        else:
            return False

    def isPalindrome4(self, x):
        if x < 0:
            return False
        strX = str(x)
        return strX == strX[::-1]