import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        product = 1
        for i, num in enumerate(nums):
            product *= num
            prefix.append(product)
        product = 1
        for i, num in enumerate(nums[::-1]):
            product *= num
            postfix.append(product)
        postfix = postfix[::-1]
        output = []
        for i in range(len(nums)):
            if i == 0:
                a = 1
            else:
                a = prefix[i-1]
            if i == len(nums) - 1:
                b = 1
            else:
                b = postfix[i+1]
            result = a * b
            output.append(result)
        return output
        