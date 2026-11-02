class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = (len(s)+1) * [False]
        dp[len(s)]= True

        for i in range(len(s),-1,-1):
            for w in wordDict:
                if (i + len(w))<=len(s) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                if dp[i]:
                    break
        
        return dp[0]