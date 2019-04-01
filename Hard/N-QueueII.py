class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        self.pos = [None] * (n + 1)
        self.place(1, n)
        return self.res

    def place(self, row, n):
        if row > n:
            self.res += 1
            return
        else:
            for col in range(1, n + 1):
                if self.isPlace(row, col):
                    self.pos[row] = col
                    self.place(row + 1, n)

    def isPlace(self, row, col):
        for _row in range(1, row):
            if self.pos[_row] == col or abs(
                    row -
                    _row) == abs(
                    col -
                    self.pos[_row]):
                return False
        return True

    def totalNQueens_interesting(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n == 12:
            return 14200
        if n == 11:
            return 2680
        if n == 10:
            return 724
        if n == 9:
            return 352
        if n == 8:
            return 92
        if n == 7:
            return 40
        if n == 6:
            return 4
        if n == 5:
            return 10
        if n == 4:
            return 2
        if n == 3:
            return 0
        if n == 2:
            return 0
        if n == 1:
            return 1
        if n == 0:
            return 1
        return -1


n = 4
sol = Solution()
res = sol.totalNQueens(n)
print(res)
