# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#  
# 
#  示例 2： 
#  
#  
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 5 * 10⁴] 内 
#  -10⁵ <= Node.val <= 10⁵ 
#  
# 
#  
# 
#  进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？ 
# 
#  Related Topics 链表 双指针 分治 排序 归并排序 👍 1758 👎 0
from typing import Optional
from leetcode.editor.cn.util import ListNode, creat_list, print_list

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(l1, l2):
            h = tail = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    tail = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    tail = l2
                    l2 = l2.next
            if l1:
                tail.next = l1
            else:
                tail.next = l2
            return h.next

        def find_mid(h):
            s1 = s2 = h
            s1_pre = None
            while s2:
                s1_pre = s1
                s1 = s1.next
                s2 = s2.next
                if s2:
                    s2 = s2.next
            s1_pre.next = None
            return s1

        if head is None:
            return None
        if head.next is None:
            return head

        mid = find_mid(head)
        # print_list(head)
        # print_list(mid)
        left_part = self.sortList(head)
        right_part = self.sortList(mid)

        return merge(left_part, right_part)


# leetcode submit region end(Prohibit modification and deletion)
head = creat_list([3, 4, 1])
Solution().sortList(head)
