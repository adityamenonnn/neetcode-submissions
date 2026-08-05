class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        value = False
        dictionary = {}
        for i in nums : 
            if i not in dictionary : 
                dictionary[i]=1
            else: 
                dictionary[i]+=1
        for key in dictionary : 
            if dictionary[key]!=1:
                return True
        return False
