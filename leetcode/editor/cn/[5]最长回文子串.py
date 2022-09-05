# 给你一个字符串 s，找到 s 中最长的回文子串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbbd"
# 输出："bb"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅由数字和英文字母组成 
#  
# 
#  Related Topics 字符串 动态规划 👍 5653 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        is_palindromic = [list([False] * n) for _ in range(n)]
        for i in range(n):
            is_palindromic[i][i] = True
        for step in range(2, n+1):
            for start in range(n):
                end = start + step - 1
                if end == n:
                    break

                if s[start] == s[end] and (start + 1 == end or is_palindromic[start+1][end-1]):
                    is_palindromic[start][end] = True

        sub_pair, sub_size = (0, 0), 1
        for i in range(n):
            for j in range(n-1, i, -1):
                if is_palindromic[i][j] and j - i + 1 > sub_size:
                    sub_pair, sub_size = (i, j), j - i + 1
                    break

        return s[sub_pair[0]: sub_pair[1]+1]



# leetcode submit region end(Prohibit modification and deletion)

res = Solution().longestPalindrome("babad")
print(res)