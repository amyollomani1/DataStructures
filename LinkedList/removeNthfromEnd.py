class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def removeNthFromEnd(head, n):
        dummy = ListNode(0, head) #creates dummy node to handle edge cases
        
        slow = dummy
        fast = head
        # or slow = fast = dummy
        
        #move fast pointer n steps ahead
        for i in range(n): #while n > 0
            fast = fast.next
           
        while fast: #goes untill fast pointer reaches end
            slow = slow.next
            fast = fast.next

        # delete or skiping nth node from end
        slow.next = slow.next.next
        
        return dummy.next
    
# Example 1
# Input: 1 -> 2 -> 3 -> 4 -> 5, n = 2
# Output: 1 -> 2 -> 3 -> 5
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
n1 = 2
result1 = removeNthFromEnd(head1, 2)
# The second node from the end is 4, so it should be removed.
# The resulting linked list should be 1 -> 2 -> 3 -> 5.
# The function should return the head of the modified linked list.
# Expected output: head1 = 1 -> 2 -> 3 -> 5