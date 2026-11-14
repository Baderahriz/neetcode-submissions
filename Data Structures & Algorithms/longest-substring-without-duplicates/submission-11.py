class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        past = set()
        for right, ch in enumerate(s):
            while ch in past:
                past.remove(s[left])
                left += 1
            else:
                past.add(ch)
                max_length = max(max_length, right - left + 1)
            
        return max_length