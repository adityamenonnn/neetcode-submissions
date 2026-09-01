class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n1 = len(s1)
        n2 = len(s2)

        frq1 = [0]*26
        frq2 = [0]*26

        for i in s1:
            frq1[(ord(i)-ord('a'))]+=1

        l = 0
        for r in range(n2):
            frq2[(ord(s2[r])-ord('a'))]+=1

            if r-l+1 > n1:
                frq2[(ord(s2[l])-ord('a'))]-=1
                l+=1
            
        
            if frq1==frq2:
                return True
        
        return False
                