# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。 
# 
#  
# 
#  
#  
#  示例 1： 
#  
#  
# 
#  
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
#  
# 
#  示例 3： 
# 
#  
# 输入：s = ""
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 3 * 10⁴ 
#  s[i] 为 '(' 或 ')' 
#  
# 
#  Related Topics 栈 字符串 动态规划 👍 1990 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 最长有效括号都是从一对括号开始向外扩充
    # 先找到所有括号对，都向外扩充，找到其中最长都可能
    def longestValidParentheses1(self, s: str) -> int:
        def expand(left, right):
            nonlocal longest
            longest = max(longest, right - left + 1)
            if left == 0:
                return
            balance = 0
            left -= 1
            weight_curr = expand_step(left)
            balance += weight_curr
            while weight_curr != 0:
                # print((left, right))
                if balance == 0:
                    expand(left, right)
                    break
                elif balance > 0:
                    right += 1
                    weight_curr = expand_step(right)
                else:
                    left -= 1
                    weight_curr = expand_step(left)
                balance += weight_curr

        def expand_step(index):
            if index in (-1, n):
                return 0
            return 1 if s[index] == '(' else - 1

        if len(s) == 0:
            return 0
        longest = 0

        n = len(s)
        for i in range(1, n):
            if s[i] == ')' and s[i-1] == '(':
                expand(i-1, i)
        return longest

    # 括号的行进描述了一座上下起伏的山脉，起点高度为0，终点高度不确定
    # '('表示向上一步，')'表示向下一步
    # 如果当前高度小于0，那么重新校准高度，下一次开始上行时记为高度1，保持高度始终大于1
    # 1.如果某一高度存在两点，那么这两点之间的括号一定能匹配
    #   （1）两点之间高度没有低于0，表示右括号数量始终没有超过左括号数量
    #   （2）上升与下降步数一致，左右括号数量一致
    # 2.匹配的最长情形一定出现在高度为0的点、极小值点或结束的时候
    #   （1）结束时能匹配的长度可能无限大，所以肯定可能出现在结尾
    #   （2）如果不是在结尾，必然在开始上升的时候，或者说极小值点
    def longestValidParentheses(self, s: str) -> int:
        height_dict = {0: -1}    # 记录之前到达该高度的点
        curr_height = 0     # 用于记录当前高度
        longest = 0         # 记录当前最大长度
        pre_long, pre_index = 0, -1
        valid_index = -1
        is_down = False

        for i, c in enumerate(s):
            # 保持高度不低于0
            if curr_height == 0 and c == ')':
                # 第一次掉到0需要处理
                if height_dict[0] != i - 1:
                    longest = max(longest, i - 1 - height_dict[0])
                valid_index = i
                height_dict[0] = i
                continue

            if c == ')':
                curr_height -= 1
                if curr_height+1 in height_dict:
                    del height_dict[curr_height+1]
                is_down = True
            else:
                curr_height += 1
                if curr_height-1 not in height_dict or height_dict[curr_height-1] < valid_index:
                    height_dict[curr_height-1] = i-1

                if is_down:
                    longest = max(longest, i-1-height_dict[curr_height-1])
                is_down = False
            # print(i, c, curr_height, longest, height_dict, pre_long, pre_index)
        last_long = len(s)-1-height_dict[curr_height] if is_down else 0
        return max(longest, last_long)

# leetcode submit region end(Prohibit modification and deletion)
print(Solution().longestValidParentheses('(())()(()(('))