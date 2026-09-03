class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0]*n

        stack = [] #[(temp,index)]
        for i in range(n):
            while stack and stack[-1][0]<temperatures[i]:   
                (temp,index)=stack.pop()
                answer[index]=i-index
            else:
                stack.append((temperatures[i],i))
        return answer