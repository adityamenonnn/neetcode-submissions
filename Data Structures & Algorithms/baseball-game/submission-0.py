class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i=="+":
                a=stack.pop()
                b=stack.pop()
                c=a+b
                stack.append(b)
                stack.append(a)
                stack.append(c)
            elif i=="C":
                stack.pop()
            elif i=="D":
                a = stack.pop()
                b= 2*a
                stack.append(a)
                stack.append(b)
            else:
                stack.append(int(i))
        return sum(stack)