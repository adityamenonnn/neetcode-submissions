class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if answer[j] == 0:
                    j = n  # no warmer day exists ahead of j either
                    break
                j += answer[j]  # jump forward, skipping resolved days
            if j < n:
                answer[i] = j - i

        return answer