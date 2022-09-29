# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数 。 
# 
#  你可以对一个单词进行如下三种操作： 
# 
#  
#  插入一个字符 
#  删除一个字符 
#  替换一个字符 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#  
# 
#  示例 2： 
# 
#  
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= word1.length, word2.length <= 500 
#  word1 和 word2 由小写英文字母组成 
#  
# 
#  Related Topics 字符串 动态规划 👍 2624 👎 0


from leetcode.editor.cn.util import print_matrix
# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # this might be redundant
        if len(word2) < len(word2):
            temp = word1
            word1 = word2
            word2 = temp

        m, n = len(word1), len(word2)
        # distance[i, j] = min distance between word1[i:] and word2[j:]
        distance = [[0] * (n + 1) for _ in range(m + 1)]
        # init distance[i, n]
        # word2 is over so delete all left part of word1, total (m-i) char
        for i in range(m):
            distance[i][n] = m - i
        # init distance[m, j]
        # word1 is over so delete all left part of word2
        for j in range(n):
            distance[m][j] = n - j

        # important
        distance[m][n] = 0

        # print_matrix(distance)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[i] == word2[j]:
                    distance[i][j] = min(distance[i+1][j]+1, distance[i][j+1]+1, distance[i+1][j+1])
                else:
                    distance[i][j] = min(distance[i+1][j]+1, distance[i][j+1]+1, distance[i+1][j+1] + 1)

        # print('==============')
        # print_matrix(distance)

        return distance[0][0]


# leetcode submit region end(Prohibit modification and deletion)

# Solution().minDistance('intention', 'execution')
# Solution().minDistance('horse', 'ros')
