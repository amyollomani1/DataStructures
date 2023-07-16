import heapq
  
def lastStoneWeight(self, stones: List[int]) -> int:
    maxHeap = [-elm for elm in stones]
    heapq.heapify(maxHeap)
    while len(maxHeap) > 1:
        y = -heapq.heappop(maxHeap) #heaviest
        x = -heapq.heappop(maxHeap) #second heaviest
        if x != y:
            heapq.heappush(maxHeap, - (y - x))
    
    if len(maxHeap) == 0:
        return 0
    return -maxHeap[0]

    """
    
    or at end do
    maxHeap.append(0)
    return abs(maxHeap[0])
    """