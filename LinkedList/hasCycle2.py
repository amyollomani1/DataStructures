class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(self, head: Optional[ListNode]) -> bool:
        def cycle_len(end):
            start, step = end, 0
            while True:
                step +=1
                start = start.next
                if start is end:
                    return step
    
        fast = slow = head
        while fast and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                #Finds start of cycle.
                cycle_len_advanced_iter = head
                for _ in range(cycle_len(slow)):
                    cycle_len_advanced_iter = cycle_len_advanced_iter.next
                it = head
                #Both iterators advance in tandem
                while it is not cycle_len_advanced_iter:
                    it = it.next
                    cycle_len_advanced_iter = cycle_len_advanced_iter.next
                return it #iter is start of cycle
        return None # no cycle
    
#Leetcode solution:
def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        
        #move slow and fast pointers
        #if theres a cycle, fast pointer will eventually meet the slw pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False