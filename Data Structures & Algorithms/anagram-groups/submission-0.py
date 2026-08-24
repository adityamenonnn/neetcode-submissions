class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            count = [0]*26
            for char in s:
                count[ord(char)-ord('a')]+=1
            
            key = tuple(count)
                
            if key not in result:
                result[key]=[]
            result[key].append(s)
        
        final = []
        for k in result:
            final.append(result[k])
        
        return final 

