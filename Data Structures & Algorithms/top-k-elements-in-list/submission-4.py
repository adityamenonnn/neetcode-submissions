class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = []
        for i in range(len(nums)+1):
            frequency.append([])

        for i in nums:
            count[i] = 1+count.get(i,0)
        
        for n,c in count.items():
            frequency[c].append(n)
        
        res = []
        for i in frequency[::-1]:
            for j in i:
                res.append(j)
                if len(res) == k:
                    return res
