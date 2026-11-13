class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        data = {}
        for i, elm in enumerate(numbers):
            val = target - elm
            if val in data:
                return [data[val]+1, i+1]
            data[elm] = i
        return data