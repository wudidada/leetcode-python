# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。 
# 
#  
#  '.' 匹配任意单个字符 
#  '*' 匹配零个或多个前面的那一个元素 
#  
# 
#  所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。 
# 
#  示例 1： 
# 
#  
# 输入：s = "aa", p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
#  
# 
#  示例 2: 
# 
#  
# 输入：s = "aa", p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "ab", p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 20 
#  1 <= p.length <= 30 
#  s 只包含从 a-z 的小写字母。 
#  p 只包含从 a-z 的小写字母，以及字符 . 和 *。 
#  保证每次出现字符 * 时，前面都匹配到有效的字符 
#  
# 
#  Related Topics 递归 字符串 动态规划 👍 3187 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def charMatch(i, j):
            nonlocal match_matrix
            # 1.首先处理越界情况
            if i >= m or j >= n:
                # 1.1 完美匹配
                if i == m and j == n:
                    return True
                # 1.2 后面还有*，有机会能匹上
                if j < n - 1 and p[j+1] == '*':
                    return charMatch(i, j+2)
                # 1.3 已耗尽，匹配失败
                return False
            # 2.两个字符串都没耗尽，需要对字符进行对比
            else:
                # print(f'{s[i:]} <-> {p[j:]}')
                # 2.1 若已知失败，不再进行后续对比(成功的话会一路返回，不用存到缓存)
                if not match_matrix[i][j]:
                    # print('match!')
                    return False
                # 2.2 字符能匹配上对应的字符或'.'
                if p[j] == '.' or s[i] == p[j]:
                    # 2.2.1 存在'*'，情况较复杂
                    if j < n - 1 and p[j+1] == '*':
                        res = charMatch(i+1, j) or charMatch(i+1, j+2) or charMatch(i, j+2)
                    # 2.2.2 不存在'*'，从下一个字符开始对比
                    else:
                        res = charMatch(i+1, j+1)
                # 2.3 字符匹配不上，但存在'*'，消耗'*'
                elif j < n - 1 and p[j+1] == '*':
                    res = charMatch(i, j+2)
                # 2.4 实在匹配不上
                else:
                    res = False
            match_matrix[i][j] = res
            return res
        m, n = len(s), len(p)
        # 存储对比结果，只会记录False，初始全置为相反的True
        match_matrix = [[True] * n for _ in range(m)]
        return charMatch(0, 0)
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().isMatch('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c'))
# print(Solution().isMatch('aab', 'a*aab'))