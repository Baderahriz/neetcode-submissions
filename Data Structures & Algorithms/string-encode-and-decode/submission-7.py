class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if strs == [""]:
            return "badereddinr"

        return "Bader***===***".join(strs)
            
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        if s == "badereddinr":
            return [""]
        return s.split("Bader***===***")
