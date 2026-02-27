""" WAP in python to group all odd and even index nodes"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
            
        odd = head
        even = head.next
        even_head = even
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
            
        odd.next = even_head
        return head
    def print_list(head):
        curr = head
        while curr:
            print(curr.val, end=" -> " if curr.next else "")
            curr = curr.next
        print()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution()
result = sol.oddEvenList(head)
print_list(result)
