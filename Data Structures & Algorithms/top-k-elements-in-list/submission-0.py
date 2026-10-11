class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hs = {}        
        mostFrequent = [[] for i in range(len(nums) + 1)]

        for n in nums:
            hs[n] = hs.get(n,0) + 1

        for n, c in hs.items():
            mostFrequent[c].append(n)
        
        res = []

        for i in range(len(mostFrequent) - 1, 0, -1):
            for n in mostFrequent[i]:
                res.append(n)
                if len(res) == k:
                    return res         