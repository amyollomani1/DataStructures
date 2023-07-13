from LinkedList import *
#returns null if there is no cycle, or returns node at start of cycle if cycle is present


class LL2(LinkedList):
    def __init__(self):
        super().__init__()
    
    def has_cycle(self):
        head = self._head
        def cycle_len(end):
            start, step = end, 0
            while True:
                step +=1
                start = start._next
                if start is end:
                    return step
    
        fast = slow = head
        while fast and fast._next and fast._next._next:
            slow, fast = slow._next, fast._next._next
            if slow is fast:
                #Finds start of cycle.
                cycle_len_advanced_iter = head
                for _ in range(cycle_len(slow)):
                    cycle_len_advanced_iter = cycle_len_advanced_iter._next
                it = head
                #Both iterators advance in tandem
                while it is not cycle_len_advanced_iter:
                    it = it._next
                    cycle_len_advanced_iter = cycle_len_advanced_iter._next
                return it #iter is start of cycle
        return None # no cycle
    
    def hasCycle(self):
        head = self._head
        mp = set()
        while head is not None:
            if head in mp:
                return True
            mp.add(head)
            head = head._next
        return False

def main():
    a_llist = LL2()
    addToList(a_llist, [1,2,3,4,1])
    print(a_llist.hasCycle())
    b_llist = LL2()
    addToList(b_llist, [1,2,1])
    print(b_llist.hasCycle())

def addToList(list, values):
    for data in values:
        list.push(data)

if __name__ == "__main__":
    main()  # This tells compiler to run the main program
 