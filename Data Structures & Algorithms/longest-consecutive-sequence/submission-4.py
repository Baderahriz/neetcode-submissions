class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numbers = set(nums)
        # print(numbers)
        lenghts = []
        current = 0
        for n in numbers:
            if n - 1 not in numbers:
                current = n
                length = 1
                while (current + 1 in numbers):
                    # print(current)
                    current += 1
                    length += 1
                lenghts.append(length)
                    
        return max(lenghts)