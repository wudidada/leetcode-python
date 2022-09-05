class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
