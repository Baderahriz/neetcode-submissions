class Solution:
    def isPalindrome(self, s: str) -> bool:
        ph = ""
        for ch in s:
            if ch.isalnum():
                ph += ch
        if len(ph) == 1:
            if ph.isspace():
                return True

        return ph.lower() == ph.lower()[::-1]