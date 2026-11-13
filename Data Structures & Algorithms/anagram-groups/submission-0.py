class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = defaultdict(list)
        for item in strs:
            s = tuple(sorted(item))
            data[s].append(item)

        return list(data.values())