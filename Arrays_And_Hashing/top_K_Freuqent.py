from collections import Counter

class Solution:  
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [x[0] for x in Counter(nums).most_common(k)]

    if __name__ == '__main__':
        print(topKFrequent(6, [1,1,1,2,2,3], 2))
      