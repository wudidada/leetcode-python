# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：n = 3
# 输出：5
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 19 
#  
# 
#  Related Topics 树 二叉搜索树 数学 动态规划 二叉树 👍 1947 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numTrees(self, n: int) -> int:
        # nums[i] record unique trees num when node num is i
        nums = [0] * (n + 1)

        # not hard to figure out nums[0] and nums[1]
        nums[0] = 1
        nums[1] = 1

        # for more complex situation
        for i in range(2, n+1):
            total = 0
            # first make the head node, n different situation
            for head in range(1, n+1):
                # in every situation, total unique num is left unique num plus right
                left_nodes = head - 1
                right_nodes = i - head
                total += nums[left_nodes] * nums[right_nodes]
            nums[i] = total
        return nums[n]
# leetcode submit region end(Prohibit modification and deletion)
