class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        for s in strs:
            frq = [0]*26
            for char in s:
                frq[ord(char)-ord('a')]+=1
            
            key = tuple(frq)
            
            if key not in count:
                count[key]=[s]
            else:
                count[key].append(s)

        res = []
        for k in count:
            res.append(count[k])
        return res



