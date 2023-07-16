import heapq

class Kth:
    def __init__(self, k, nums):
        self.k = k
        sorted(nums)
        self.nums = nums

    def add(self,val):
        arr = self.nums
        arr.append(val)
        sorted(self.nums)
        return arr[self.k-1]
    
#Leetcode answer
class kthLargest:
    #in original array, finding kth largest takes O(n)
    #in sorted array, finding kth largest takes O(logn) - using binary search
        #problem: insertions take O(n)
    #so use a minheap instead
    """
    min heap: add/pop is logn. finding min is O(1)
    """
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        #turn array into heap
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) # this keeps the k largest
            
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        
        