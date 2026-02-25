"""LEETCODE QUESTION 1: You have been given two non empty linked lists representing two non=negative integer . The digits are stored in reverse order and each of their nodes contains a single digit 
and then add two numbers and return their sum as linked list """

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            
            curr.next = ListNode(total % 10)
            curr = curr.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

    def print_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

sol = Solution()
result = sol.addTwoNumbers(l1, l2)

print_list(result)
