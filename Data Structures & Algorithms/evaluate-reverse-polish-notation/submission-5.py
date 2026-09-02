class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                a=stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif i == '*':
                a=stack.pop()
                b = stack.pop()
                stack.append(a*b)
            elif i == '-':
                a=stack.pop()
                b = stack.pop()
                stack.append(b-a) #b-a as the first popped is right operand, and secodn is left
            elif i == '/':
                a=stack.pop()
                b = stack.pop()
                stack.append(int(b/a)) #truncates down
            else:
                stack.append(int(i))
        return stack[-1]