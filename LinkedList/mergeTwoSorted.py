from LinkedList import *

class LL(LinkedList):
    def __init__(self):
        super().__init__()
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        #this class initlizes first node to 0. thats why to return the real "head" of this list do .next
    """
    class Solution:
        def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
            res = ListNode()
            tail = res #need this so that you can return res at the end

            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next

            if list1:
                tail.next = list1
            elif list2:
                tail.next = list2

            return res.next
    """
    #chatGPT duplicates allowed
    def mergeTwoSortLists(self,l1, l2):
        res = LL()
        curr1 = l1.head
        curr2 = l2.head
        
        while curr1 and curr2:
            if curr1.data <= curr2.data:
                res.append(curr1.data)
                curr1 = curr1.next
            else:
                res.append(curr2.data)
                curr2 = curr2.next
                
        while curr1:
            res.append(curr1.data)
            curr1 = curr1.next
        while curr2:
            res.append(curr2.data)
            curr2 = curr2.next
            
        return res
   

def main():
    l1 = LL()
    l2 = LL()
    l1.createList([1,2,5,8,9,11])
    l2.createList([2,3,4,10,12])
    
    l3 = l1.mergeTwoSortLists(l1, l2)
    l3.print_list()

if __name__ == "__main__":
    main()