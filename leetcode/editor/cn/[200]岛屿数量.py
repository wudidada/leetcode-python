# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] 的值为 '0' 或 '1' 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 1957 👎 0

from typing import List

from leetcode.editor.cn.util import print_matrix
# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def traverse(x, y):
            if x >= m or x < 0 or y < 0 or y >= n or grid[x][y] == '0' or matrix[x][y]:
                return

            matrix[x][y] = True
            # print(f'=============={x}:{y}')
            # print_matrix(matrix)
            traverse(x+1, y)
            traverse(x-1, y)
            traverse(x, y+1)
            traverse(x, y-1)

        res = 0
        m, n = len(grid), len(grid[0])
        matrix = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not matrix[i][j]:
                    res += 1
                    traverse(i, j)
        return res


# leetcode submit region end(Prohibit modification and deletion)

print(Solution().numIslands([["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]))
