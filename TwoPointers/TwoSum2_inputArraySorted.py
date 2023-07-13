def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1 

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        
        """#Same effectivness
        nums_dict = {}

        for i, num in enumerate(numbers):
            t = target - num

            if t in nums_dict:
                return [nums_dict[t] + 1, i + 1]
            
            nums_dict[num] = i
            """