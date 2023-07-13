
#constraints: 1 <= nums[i] <= n and nums.length == n+1
#don't modify actual array

#my way that I made up, problem: it modifies array
def findDuplicate(self, nums: List[int]) -> int:
    n = len(nums)
    for i in range(n):
        #taking abs val and subtracting 1 makes sure its inside correct index
        index = (abs(nums[i]) - 1) % n 
        if nums[index] < 0: # if neg = visted means duplicate
            return abs(nums[i])
        nums[index] *= -1 #multiple number at array with negative to mark it as visitied
                
#ChatGBT
def findDuplicate(nums):
    n = len(nums) - 1
    left = 1
    right = n

    #implements binary search
    while left <= right:
        mid = (left + right) // 2
        #counts num of elm in nus <= to mid
        count = sum(1 for num in nums if num <= mid)

        if count > mid: #then repeated num in range [left,mid]
            right = mid - 1
        else: #then its in [mid+1, right]
            left = mid + 1

    return left

#leetcode answer
def findDuplicate(self, nums: List[int]) -> int:
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]] #this moves fast two steps at a time
        if slow == fast:
            #at this point, theres a cycle in array aka: meeting point
            #since fast will overlap slow
            break 

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow





