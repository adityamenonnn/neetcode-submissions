class TimeMap:

    def __init__(self):  
        self.hashMap = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashMap:
            self.hashMap[key].append([value,timestamp])
        else:
            self.hashMap[key]=[]
            self.hashMap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap:
            return ""
        
        res = ""
        values = self.hashMap[key]
        l = 0 
        r = len(values)-1
        while l<=r:
            mid = (l+r)//2
            if timestamp>=values[mid][-1]:
                res = values[mid][0]
                l = mid+1
            else:
                r = mid - 1
        return res
            

        

