class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = []
        for i in range(len(nums)+1):
            frequency.append([])
        
        for i in nums : 
            count[i]=1+count.get(i,0)

        for n,c in count.items():
            frequency[c].append(n)

        
        result = []
        for i in range(len(frequency)-1,0,-1):
            for n in frequency[i]:
                result.append(n)
                if len(result)==k:
                    return result


