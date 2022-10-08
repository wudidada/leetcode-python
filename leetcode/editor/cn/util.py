import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree(nums):
    if not nums:
        return

    def create_node(i):
        if i >= n:
            return
        node = TreeNode(nums[i])
        node.left = create_node(i * 2 + 1)
        node.right = create_node(i * 2 + 2)

        return node

    n = len(nums)
    return create_node(0)


def creat_list(nums):
    head = tail = ListNode()
    for num in nums:
        tail.next = ListNode(num)
        tail = tail.next
    return head.next


def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)


def print_matrix(matrix):
    for row in matrix:
        print(row)
