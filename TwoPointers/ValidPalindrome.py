class Solution:
    def isPalindrome(self, s: str) -> bool:
        """#this solution is faster
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
        """
        s = s.lower()
        new = re.sub(r"[\W_]+|[\s]+","",s) #removes numbers and other things from words
        # splitted  = subbed.split()
        return new == new[::-1] #returns true if word is symmetric
    
    