# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
#  
# 
#  示例 2： 
# 
#  
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == height.length 
#  1 <= n <= 2 * 10⁴ 
#  0 <= height[i] <= 10⁵ 
#  
# 
#  Related Topics 栈 数组 双指针 动态规划 单调栈 👍 3781 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    # 只适合高度较小情况
    def trap1(self, height: List[int]) -> int:
        height_dict = {}
        res = 0
        for i, h in enumerate(height):
            for _ in range(1, h + 1):
                if _ in height_dict:
                    res += i - height_dict[_] - 1
                height_dict[_] = i
        return res

    def trap(self, height: List[int]) -> int:
        height_stack = []
        res = 0
        for i, h in enumerate(height):
            valid_height = 0
            while len(height_stack):
                pre_i, pre_h = height_stack[-1]
                if h >= pre_h:
                    res += (pre_h - valid_height) * (i - pre_i - 1)
                    valid_height = height_stack.pop()[1]
                else:
                    res += (h-valid_height) * (i - pre_i - 1)
                    height_stack.append((i, h))
                    break
            # print((i, h), valid_height, res)

            if len(height_stack) == 0:
                height_stack.append((i, h))

        return res


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().trap([4,2,0,3,2,5]))
