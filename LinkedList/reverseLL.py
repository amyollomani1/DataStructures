from LinkedList import *

class LL(LinkedList):
    def __init__(self):
        super().__init__()
        
    #Leetcode answer
    def reverse(self):
        prev, curr = None, self.head  
        while curr:
            temp = curr.next
            curr._next = prev
            prev = curr
            curr = temp
        return prev
    
    #ChatGPT 
    def reverse2(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        
def main():
    a_llist = LL()
    a_llist.createList([1,2,3,4])
    a_llist.print_list()
    a_llist.reverse2()
    a_llist.print_list()
    
    """"""""
    b_llist = LL()
    b_llist.createList([2,3,4])
    b_llist.print_list()
    b_llist.reverse()
    b_llist.print_list()
    

if __name__ == "__main__":
    main()