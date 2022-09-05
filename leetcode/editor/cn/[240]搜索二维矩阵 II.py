# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性： 
# 
#  
#  每行的元素从左到右升序排列。 
#  每列的元素从上到下升序排列。 
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21
# ,23,26,30]], target = 5
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21
# ,23,26,30]], target = 20
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= n, m <= 300 
#  -10⁹ <= matrix[i][j] <= 10⁹ 
#  每行的所有元素从左到右升序排列 
#  每列的所有元素从上到下升序排列 
#  -10⁹ <= target <= 10⁹ 
#  
# 
#  Related Topics 数组 二分查找 分治 矩阵 👍 1110 👎 0


from typing import List
# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        def search(i, j):
            nonlocal too_small, too_big
            if i == max_i or j == max_j:
                return
            pos = (i, j)
            if pos[0] >= too_big[0] and pos[1] >= too_big[1]:
                return
            if pos[0] <= too_small[0] and pos[1] <= too_small[1]:
                return search(i, j+1)

            ele = matrix[i][j]
            # print(ele)
            if ele == target:
                return True
            elif ele < target:
                too_small = pos
            else:
                too_big = pos
            return search(i+1, j) or search(i, j+1)

        max_i = len(matrix)
        max_j = len(matrix[0])
        too_big = (max_i, max_j)
        too_small = (-1, -1)
        return search(0, 0)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = m-1, 0
        while i >= 0 and j < n:
            ele = matrix[i][j]
            if ele == target:
                return True
            elif ele > target:
                i -= 1
            else:
                j += 1
        return False

# leetcode submit region end(Prohibit modification and deletion)
Solution().searchMatrix([[-1, 3]], 3)