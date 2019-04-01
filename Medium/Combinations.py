class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        out = []
        self.helper(n, k, 1, out)
        return self.res

    def helper(self, n, k, start, out: list):
        if len(out) == k:
            self.res.append(out[:])
            return
        for i in range(start, n + 1):     # try each possibility number in current position
            out.append(i)
            self.helper(n, k, i + 1, out)
            out.pop()

    def combine2(self, n, k):
        if k == 0:
            return [[]]
        return [x + [tail] for tail in range(n, k - 1, -1) for x in self.combine(tail - 1, k - 1)]

    def combine2(self, n, k):
        res = []



n = 4
k = 2
solution = Solution()
reT = solution.combine(n, k)
print(reT)
