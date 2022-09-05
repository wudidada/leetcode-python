# 给你一个链表数组，每个链表都已经按升序排列。 
# 
#  请你将所有链表合并到一个升序链表中，返回合并后的链表。 
# 
#  
# 
#  示例 1： 
# 
#  输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#  
# 
#  示例 2： 
# 
#  输入：lists = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  输入：lists = [[]]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  k == lists.length 
#  0 <= k <= 10^4 
#  0 <= lists[i].length <= 500 
#  -10^4 <= lists[i][j] <= 10^4 
#  lists[i] 按 升序 排列 
#  lists[i].length 的总和不超过 10^4 
#  
# 
#  Related Topics 链表 分治 堆（优先队列） 归并排序 👍 2142 👎 0


import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional, List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == [] or not any(lists):
            return None

        lists_copy = list(_ for _ in lists if _ is not None)

        remains_cnt = len(lists_copy)
        heap = [(a.val, i) for i, a in enumerate(lists_copy)]
        heapq.heapify(heap)

        res = last_node = None

        while remains_cnt:
            element = heapq.heappop(heap)
            if res is None:
                res = last_node = ListNode(element[0])
            else:
                temp = ListNode(element[0])
                last_node.next = temp
                last_node = temp

            index = element[1]
            lists_copy[index] = lists_copy[index].next
            if lists_copy[index] is None:
                remains_cnt -= 1
            else:
                heapq.heappush(heap, (lists_copy[index].val, index))

        return res

# leetcode submit region end(Prohibit modification and deletion)
