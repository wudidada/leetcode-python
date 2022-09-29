# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]
# ,["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = []
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：matrix = [["0"]]
# 输出：0
#  
# 
#  示例 4： 
# 
#  
# 输入：matrix = [["1"]]
# 输出：1
#  
# 
#  示例 5： 
# 
#  
# 输入：matrix = [["0","0"]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  rows == matrix.length 
#  cols == matrix[0].length 
#  1 <= row, cols <= 200 
#  matrix[i][j] 为 '0'  或 '1'
#  
# 
#  Related Topics 栈 数组 动态规划 矩阵 单调栈 👍 1368 👎 0


from typing import List
# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        从上到下一行一行遍历数组 合并上一行中与当前行中为1的区域
        合并时可能造成之前区域变窄，需要记录之前区域的高度
        同时也要记录当前行中为1的区域，有可能最大区域从这一行开始
        :param matrix:
        :return:
        """
        def range_row(row):
            index = 0
            row_list = matrix[row]
            range_dict = {}
            while index < n:
                if row_list[index] == '1':
                    start = index
                    while index < n and row_list[index] == '1':
                        index += 1
                    range_dict[(start, index-1)] = index - start
                index += 1
            return range_dict

        max_dict = {}
        max_size = 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            new_max_dict = {}
            curr_dict = range_row(i)
            for pre_range, (pre_size, pre_len) in max_dict.items():
                if pre_range in curr_dict:
                    new_max_dict.update({pre_range: (pre_size+curr_dict[pre_range], pre_len+1)})
                    max_size = max(max_size, pre_size+curr_dict[pre_range])
                    continue

                for curr_range, curr_size in curr_dict.items():
                    merge_range = (max(curr_range[0], pre_range[0]), min(curr_range[1], pre_range[1]))
                    if merge_range[1] < merge_range[0]:
                        continue

                    new_len = pre_len + 1
                    new_size = (merge_range[1]-merge_range[0]+1) * new_len
                    if merge_range in new_max_dict and new_size < new_max_dict[merge_range][0]:
                        continue

                    new_max_dict[merge_range] = (new_size, new_len)

                    max_size = max(max_size, new_size)

            max_dict = new_max_dict
            for curr_range, curr_size in curr_dict.items():
                if curr_range not in max_dict:
                    max_dict.update({curr_range: (curr_size, 1)})
                    max_size = max(max_size, curr_size)

            # print(matrix[i], max_size, max_dict)

        return max_size

# leetcode submit region end(Prohibit modification and deletion)
Solution().maximalRectangle([["1","0","1","1","1","0","0","0","1","0"],["0","1","0","0","0","0","0","1","1","0"],["0","1","0","1","0","0","0","0","1","1"],["1","1","1","0","0","0","0","0","1","0"],["0","1","1","1","0","0","1","0","1","0"],["1","1","0","1","1","0","1","1","1","0"]])
