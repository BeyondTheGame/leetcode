class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        _set = set()
        _sum = 0
        while _sum != 1:
            _sum = 0
            while n:
                _sum += pow(n % 10, 2)
                n = n//10
            n = _sum
            if n in _set:
                return False
            _set.add(n)
        return _sum == 1

    def isHappy2(self, n):
        """
        其实这道题也可以不用set来做，我们并不需要太多的额外空间，关于非快乐数有个特点，
        循环的数字中必定会有4，这里就不做证明了，我也不会证明，就是利用这个性质，就可以不用set了，
        :param n:
        :return:
        """
        _sum = 0
        while _sum != 1 and _sum != 4:
            _sum = 0
            while n:
                _sum += pow(n % 10, 2)
                n = n//10
            n = _sum
        return _sum == 1