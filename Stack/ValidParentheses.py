class Solution:
    def isValid(self, s: str) -> bool:
        #keys are closing
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in Map:
                if stack and stack[-1] == Map[c]:
                    stack.pop()
                else:
                    return False
            else: #if its an open parenthes
                stack.append(c)

        return True if not stack else False

        #if stack checks that stack isn't empty
        
        
        
