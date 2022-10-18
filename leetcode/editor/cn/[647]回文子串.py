# 给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。 
# 
#  回文字符串 是正着读和倒过来读一样的字符串。 
# 
#  子字符串 是字符串中的由连续字符组成的一个序列。 
# 
#  具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa" 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 由小写英文字母组成 
#  
# 
#  Related Topics 字符串 动态规划 👍 990 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        matrix = [[False] * n for _ in range(n)]
        for _ in range(n):
            matrix[_][_] = True

        res = 0
        for i in range(n):
            for j in range(0, i+1):
                if s[i] == s[j]:
                    if j + 1 > i - 1 or matrix[j+1][i-1]:
                        res += 1
                        matrix[j][i] = True
                        # print(s[j:i+1])
        return res
# leetcode submit region end(Prohibit modification and deletion)

print(Solution().countSubstrings("fdsklf"))