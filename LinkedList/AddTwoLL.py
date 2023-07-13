class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
# Example: l1 = [2,4,3] l2 = [5,6,4] answer = [7,0,8] since 342 + 465 = 807
#note: LL is in reverse order

#Leetcode answer
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

#ChatGPT answer

def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    carry = 0

    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        summ = x + y + carry
        
        #// operator represents floor division. returns quotient
        # ie: (7 + 5) // 10 results in 1 as quotient with remainder 2
        carry = summ // 10 
        
        #sum %10 calculates the remainder when sum is divided by 10
        curr.next = ListNode(summ % 10) 
        curr = curr.next

        if l1:
            l1 = l1.next
        if l2:
            l2= l2.next

    if carry > 0:
        curr.next = ListNode(carry)

    return dummy.next
