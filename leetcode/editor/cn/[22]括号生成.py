# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：["()"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 8 
#  
# 
#  Related Topics 字符串 动态规划 回溯 👍 2850 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    # 错误的做法，无法生成(()())括号嵌套类型
    def generateParenthesis1(self, n: int) -> List[str]:
        def plus(left, right_index):
            return [[left, *a] for a in res[right_index]]

        res = [[[1]]]
        for i in range(1, n):
            res_curr = []
            for j in range(1, i + 1):
                res_curr.extend(plus(j, i - j))
            res_curr.append([i + 1])
            res.append(res_curr)
        # print(res)
        p_array = tuple(map(lambda a: f'{"(" * a}{")" * a}', range(n + 1)))
        return ["".join([p_array[_] for _ in one_res]) for one_res in res[-1]]

    def generateParenthesis(self, n: int) -> List[str]:
        def generate(curr):
            nonlocal left, right, res
            if left == 0 and right == 0:
                res.append(''.join(curr))
                return

            if left > right or left < 0 or right < 0:
                return

            curr.append('(')
            left -= 1
            generate(curr)
            curr.pop()
            left += 1

            curr.append(')')
            right -= 1
            generate(curr)
            curr.pop()
            right += 1

        left, right = n, n
        res = []
        generate([])
        return res


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().generateParenthesis(3))
