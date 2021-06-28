# 给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看
# 做它自身的一棵子树。 
# 
#  示例 1: 
# 给定的树 s: 
# 
#  
#      3
#     / \
#    4   5
#   / \
#  1   2
#  
# 
#  给定的树 t： 
# 
#  
#    4 
#   / \
#  1   2
#  
# 
#  返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。 
# 
#  示例 2: 
# 给定的树 s： 
# 
#  
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
#  
# 
#  给定的树 t： 
# 
#  
#    4
#   / \
#  1   2
#  
# 
#  返回 false。 
#  Related Topics 树 深度优先搜索 二叉树 字符串匹配 哈希函数 
#  👍 514 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, t1, t2):
        if not t1 and not t2:
            return True
        elif not t1 or not t2:
            return False

        if t1.val != t2.val:
            return False

        return self.isSameTree(t1.left, t2.left) and self.isSameTree(t1.right, t2.right)

# leetcode submit region end(Prohibit modification and deletion)
