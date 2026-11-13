class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # data = {}
        # for i, elm in enumerate(numbers):
        #     val = target - elm
        #     if val in data:
        #         return [data[val]+1, i+1]
        #     data[elm] = i
        # return data
        right = len(numbers) - 1 
        left = 0
        while True:
            result = numbers[left] + numbers[right]
            if result > target:
                right -= 1
            elif result < target:
                left += 1
            if result == target:
                return [left+1, right+1]