#0 ,1 ,2 ,3 ... , n-1, n
#resutl: 0, n, 1, n-1, 2, n-2

def main():
    #TC: O(n) SC: O(1) #do in place
    
    """
    
    1 way to do this with extra memory is to split list in half. 
    then have two pointers, 1 starting at beginning of first, and other at end of second
    Then create new list 
    
    To do in place:
    Reverse the second half of the list
    1 -> 2 -> 3 -> 4   make is so 4 points to 3, so we can iterate to it
    Find middle using a fast and slow pointer.
    
    """
    #find middle
    slow, fast= head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    #reverse second half
    second = slow.next
    prev = slow.next = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = temp
    
    #merge two halfs
    second = prev
    first = head
    while second:
         tmp1, tmp2 = first.next, second.next
         first.next = second
         second.next = tmp1
         first = tmp1
         second = tmp2
         
    