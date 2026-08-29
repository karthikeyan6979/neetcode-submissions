class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        n = len(nums)
        buckets = [[] for _ in range(n+1)]
        for i in nums:
            count[i] += 1
        for i, c in count.items():
            if buckets[c] == 0:
                buckets[c] = [i]
            else:
                buckets[c].append(i)
        res = []
        for i in range(n, -1, -1):
            if buckets[i] != 0:
                res.extend(buckets[i])
            if len(res) == k:
                break
        return res