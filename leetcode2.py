""" LEETCODE QUESTION 2: Write a code in Python to merge two linked list after sorting them  """

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        curr.next = list1 or list2
        
        return dummy.next

    def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "")
        curr = curr.next
    print()

l1 = ListNode(1, ListNode(2, ListNode(4)))

l2 = ListNode(1, ListNode(3, ListNode(4)))

sol = Solution()
merged_head = sol.mergeTwoLists(l1, l2)

printList(merged_head)
