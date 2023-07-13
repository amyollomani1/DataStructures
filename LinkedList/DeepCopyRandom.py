class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

#difference between this and a normal linked list is that theres another random pointer, that points to a random node in list
#make deep copy: create a new list with new nodes

def copyRandomList(self, head: "Node") -> "Node":
    
    """
    Make two passes
    First pass: 
    use a hashmap that maps original nodes to corresponding new nodes. This will help establish correct connections later
    Iterte through original and create a new node for each original node (set correct vals here)
    
    Iterate original again: 
    for each oroginal node, set next pointer corresponding to new node
    Also set correct random pointers
    
    """
    
    #hashmap
    oldToCopy = {None: None} #this adds so that Null points to Null node hashmap

    cur = head
    while cur:
        copy = Node(cur.val) #this is a deep copy of node
        oldToCopy[cur] = copy #add corresponding copy to hashmap
        cur = cur.next
    cur = head
    while cur:
        copy = oldToCopy[cur] #this gives copy
        copy.next = oldToCopy[cur.next]
        copy.random = oldToCopy[cur.random]
        cur = cur.next
        
    return oldToCopy[head]

#Time complexity: O(n) SC: O(n) since we use a hashmap
