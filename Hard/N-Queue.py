class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        self.pos = [None]*(n+1)     # pos[i] 表示第i行的皇后所在的列
        self.place(1, n)
        return self.res

    def place(self, row, n):
        """
        放置皇后到棋盘上
        :param row:   第k行
        :param n:   总共的行数
        :return:
        """
        if row > n:     # 找到一组解
            self.putOneSloveInRes(n)
            return
        else:
            for col in range(1, n+1):    # 试探第row行的每一个列
                if self.isPlace(row, col):
                    self.pos[row] = col
                    self.place(row+1, n)

    def isPlace(self, row, col):
        """
        判断在(row, col)的位置上是否可以放置皇后
        :param row:
        :param col:
        :return:
        """
        for _row in range(1, row):   # 1---(row-1)是已经放置了皇后的行
            if self.pos[_row] == col or abs(row - _row) == abs(col - self.pos[_row]):
                return False
        return True

    def putOneSloveInRes(self, n):
        """
        将一组解放置到返回结果中去
        :return:
        """
        out = [['.' for col in range(n)] for row in range(n)]
        re = []
        for row in range(1, n+1):
            col = self.pos[row]
            out[row-1][col - 1] = 'Q'
            re.append("".join(out[row-1]))
        self.res.append(re)

    def solveNQueens2(self, n):
        self.res = []
        self.pos = [None] * (n + 1)  # pos[i] 表示第i行的皇后所在的列
        row = 1
        col = 1
        while row <= n:
            while col <= n:
                if self.isPlace(row, col):
                    self.pos[row] = col
                    col = 1
                    break
                else:
                    col += 1
            if self.pos[row] is None:   # 在第row没有找到位置, 回溯
                if row == 1:    # 回溯到第一行，仍然无法找到可以放置皇后的位置，则说明已经找到所有的解，程序终止
                    break
                else:
                    row -= 1
                    col = self.pos[row] + 1     # 把上一行皇后的位置往后移一列
                    self.pos[row] = None    # 把上一行皇后的位置清除，重新探测
                    continue
            if row == n:    # 找到一个方案
                self.putOneSloveInRes(n)
                col = self.pos[row] + 1     # 从最后一行放置皇后列数的下一列继续探测
                self.pos[row] = None    # 清除最后一行的皇后位置
                continue
            row += 1
        return self.res







n = 4
sol = Solution()
res = sol.solveNQueens2(n)
print(res)