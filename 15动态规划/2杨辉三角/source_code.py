from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        g = [[1] * (i + 1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                g[i][j] = g[i - 1][j - 1] + g[i - 1][j]  # 左上方的数 + 右上方的数
        return g
    