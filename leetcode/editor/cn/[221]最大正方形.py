# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]
# ,["1","0","0","1","0"]]
# 输出：4
#  
# 
#  示例 2： 
#  
#  
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：matrix = [["0"]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 300 
#  matrix[i][j] 为 '0' 或 '1' 
#  
# 
#  Related Topics 数组 动态规划 矩阵 👍 1291 👎 0


from typing import List
from leetcode.editor.cn.util import print_matrix
# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])

        size = [[0] * n for _ in range(m)]
        size[0] = list(map(int, matrix[0]))
        res = max(size[0])
        for _ in range(m):
            size[_][0] = int(matrix[_][0])
            res = max(res, size[_][0])

        for i in range(1, m):
            for j in range(1, n):
                if size[i-1][j] == 0 or size[i][j-1] == 0 or size[i-1][j-1] == 0 or matrix[i][j] == "0":
                    size[i][j] = int(matrix[i][j])
                else:
                    size[i][j] = min(size[i-1][j-1], size[i-1][j], size[i][j-1]) + 1
                    # print(f'--------{i}:{j}-----------')
                    # print_matrix(size)

                res = max(res, size[i][j]**2)

        return res

# leetcode submit region end(Prohibit modification and deletion)
Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])