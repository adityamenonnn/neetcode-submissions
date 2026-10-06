class Solution:
    def isValid(self, s: str) -> bool:
        match = {'}':'{',')':'(',']':'[' }

        stack = []

        for i in s:
            if i not in match:
                stack.append(i)
            else:
                if stack and stack[-1]==match[i]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False