class Solution:
    def containsDuplicate(self, nums: list[int]) ->bool:
        hashset = set() #declaring hashset
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

    if __name__ == '__main__':
        print(containsDuplicate(4, [1,2,3,1]))
        print(containsDuplicate(3, [1,2,3]))
