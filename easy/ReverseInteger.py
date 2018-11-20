class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        xlist = list(str(x))
        xlist.reverse()
        if xlist[-1] == '-':   # 是负数
            xlist.pop()
            ans = -int(''.join(xlist))
        else:
            ans = int(''.join(xlist))
        if ans > 2**31-1 or ans < -2**31:   # the reversed integer overflows.
            return 0
        else:
            return ans

    def reverse2(self, x):
        if x == 0:
            return 0
        if x < 0:
            flag = -1
        else:
            flag = 1
        x = abs(x)
        xlist = list(str(x))
        xlist.reverse()
        ans = flag * int(''.join(xlist))
        if ans > 2 ** 31 - 1 or ans < -2 ** 31:
            return 0
        else:
            return ans

    def reverse3(self, x):
        flag = -1 if x < 0 else 1
        x = abs(x)
        ans = 0
        while x:
            ans, x = ans * 10 + x % 10, x // 10
        return ans * flag if -2 ** 31 < ans * flag < 2 ** 31-1 else 0

    def reverse4(self, x):
        if x < 0:
            ans = -1*int(str(-x)[::-1])
        else:
            ans = int(str(x)[::-1])
        return ans if -2**31 < ans < 2**31-1 else 0
