class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        result = []
        for num in nums:
            if num not in freqs:
                freqs[num] = 1
            else:
                freqs[num] += 1
        freqs = sorted(freqs.items(), key=lambda x:x[1], reverse=True)
        for i in range(0, k):
            result.append(freqs[i][0])
        return result