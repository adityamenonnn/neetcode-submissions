class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = [] #will have all the times that it takes
        pairs = []

        for p in range(len(position)):
            pairs.append([position[p],speed[p]])
        
        pairs.sort()

        for p,s in pairs[::-1]:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
            
        return len(stack)
            