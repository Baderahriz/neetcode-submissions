class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}
        keys = set(nums)
        for elm in keys:
            data[elm] = 0
        for n in nums:
            data[n] += 1

        values = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
        return ((list(values.keys()))[:k])